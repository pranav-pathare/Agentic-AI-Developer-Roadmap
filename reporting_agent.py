"""
Offline Reporting Agent
-----------------------
Automates reporting WITHOUT any internet or API key. Instead of asking a cloud
LLM which tool to run, a small rule-based parser reads your plain-English request
and routes it to local "tools": load data, analyze it, chart it, render an HTML
report, and (offline) draft an email.

This mirrors the tool set in reporting-agent-project.md, but the "brain" is a
deterministic parser rather than Gemini — so it runs with no network.

Dependencies: none required. Uses these ONLY if installed:
    openpyxl    -> read .xlsx files (else CSV only)
    matplotlib  -> render chart PNGs (else charts are skipped with a note)

Usage:
    python reporting_agent.py data.csv                 # interactive loop
    python reporting_agent.py data.csv "report"        # one-shot
    python reporting_agent.py data.csv "top 5 product by revenue, chart"
    python reporting_agent.py data.csv "sum revenue, report, email to sam@x.com"
"""

import csv
import os
import re
import sys
from datetime import datetime
from statistics import mean

REPORTS_DIR = "reports"


# --------------------------------------------------------------------------- #
# Tool 1: load_data — read CSV (stdlib) or XLSX (openpyxl if available)
# --------------------------------------------------------------------------- #
def _find_header_row(all_rows, look=15):
    """Find the real header row, skipping metadata/blank preamble lines.

    Some real exports start with title/date rows before the column names.
    Heuristic: among the first `look` rows, pick the one with the most non-empty
    cells — that's almost always the true header — preferring the earliest tie.
    """
    best_idx, best_score = 0, -1
    for i, row in enumerate(all_rows[:look]):
        score = sum(1 for c in row if str(c).strip())
        if score > best_score:
            best_idx, best_score = i, score
    return best_idx


def load_data(path):
    """Load a CSV or XLSX file into (rows, columns).

    rows    -> list of dicts, one per record, keyed by column name
    columns -> list of column names in order
    """
    ext = path.lower().rsplit(".", 1)[-1]
    if ext == "csv":
        with open(path, newline="", encoding="utf-8", errors="replace") as f:
            all_rows = list(csv.reader(f))
        header_idx = _find_header_row(all_rows)
        columns = [c.strip() for c in all_rows[header_idx]]
        rows = [
            {columns[i]: r[i] for i in range(min(len(columns), len(r)))}
            for r in all_rows[header_idx + 1:]
            if any(cell.strip() for cell in r)  # skip fully blank lines
        ]
    elif ext in ("xlsx", "xlsm"):
        try:
            from openpyxl import load_workbook
        except ImportError:
            raise SystemExit(
                "Reading .xlsx needs openpyxl. Install it (pip install openpyxl) "
                "or export the sheet to .csv."
            )
        wb = load_workbook(path, data_only=True)
        ws = wb.active
        data = list(ws.iter_rows(values_only=True))
        if not data:
            return [], []
        columns = [str(c) if c is not None else f"col{i}" for i, c in enumerate(data[0])]
        rows = [
            {columns[i]: ("" if v is None else v) for i, v in enumerate(r)}
            for r in data[1:]
        ]
    else:
        raise SystemExit(f"Unsupported file type: .{ext} (use .csv or .xlsx)")
    return rows, columns


# --------------------------------------------------------------------------- #
# Small helpers for typing / numeric columns
# --------------------------------------------------------------------------- #
def _to_number(value):
    """Return a float if the value looks numeric, else None."""
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip().replace(",", "").replace("$", "").replace("%", "")
    try:
        return float(s)
    except ValueError:
        return None


def numeric_columns(rows, columns):
    """Columns where most non-empty values parse as numbers."""
    numeric = []
    for col in columns:
        vals = [_to_number(r.get(col)) for r in rows]
        got = [v for v in vals if v is not None]
        nonempty = [r.get(col) for r in rows if r.get(col) not in (None, "")]
        if nonempty and len(got) >= 0.8 * len(nonempty):
            numeric.append(col)
    return numeric


def _column(rows, col):
    """All numeric values in a column, skipping blanks/non-numbers."""
    return [n for n in (_to_number(r.get(col)) for r in rows) if n is not None]


def _resolve_column(name, columns):
    """Case-insensitive / partial match of a spoken column name to a real one."""
    if not name:
        return None
    name = name.strip().lower()
    for c in columns:
        if c.lower() == name:
            return c
    for c in columns:
        if name in c.lower():
            return c
    return None


# --------------------------------------------------------------------------- #
# Tool 2: run_analysis — aggregate / top-N / group-by
# --------------------------------------------------------------------------- #
def summarize(rows, columns):
    """Overall summary: row count + stats for each numeric column."""
    nums = numeric_columns(rows, columns)
    stats = []
    for col in nums:
        vals = _column(rows, col)
        if vals:
            stats.append(
                {
                    "column": col,
                    "count": len(vals),
                    "sum": sum(vals),
                    "mean": mean(vals),
                    "min": min(vals),
                    "max": max(vals),
                }
            )
    return {"rows": len(rows), "numeric": stats}


def aggregate(rows, op, col):
    """Run one aggregation (sum/mean/min/max/count) on a numeric column."""
    if op == "count":
        return len(rows)
    vals = _column(rows, col)
    if not vals:
        return None
    return {"sum": sum, "mean": mean, "min": min, "max": max}[op](vals)


def group_by(rows, group_col, value_col, op="sum"):
    """Group rows by group_col and aggregate value_col per group."""
    buckets = {}
    for r in rows:
        key = str(r.get(group_col, "")).strip() or "(blank)"
        n = _to_number(r.get(value_col))
        if n is not None:
            buckets.setdefault(key, []).append(n)
    fn = {"sum": sum, "mean": mean, "min": min, "max": max}[op]
    result = {k: fn(v) for k, v in buckets.items()}
    return dict(sorted(result.items(), key=lambda kv: kv[1], reverse=True))


def top_n(rows, label_col, value_col, n=5):
    """Top N rows by a numeric column, as (label, value) pairs."""
    scored = []
    for r in rows:
        v = _to_number(r.get(value_col))
        if v is not None:
            scored.append((str(r.get(label_col, "")), v))
    scored.sort(key=lambda t: t[1], reverse=True)
    return scored[:n]


# --------------------------------------------------------------------------- #
# Tool 3: make_chart — bar chart PNG (matplotlib if available)
# --------------------------------------------------------------------------- #
def make_chart(pairs, title, filename):
    """Save a bar chart from (label, value) pairs. Returns path or None."""
    try:
        import matplotlib

        matplotlib.use("Agg")  # no display needed — works headless/offline
        import matplotlib.pyplot as plt
    except ImportError:
        return None
    if not pairs:
        return None
    os.makedirs(REPORTS_DIR, exist_ok=True)
    labels = [str(p[0]) for p in pairs]
    values = [p[1] for p in pairs]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(labels, values, color="#4C78A8")
    ax.set_title(title)
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    path = os.path.join(REPORTS_DIR, filename)
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
# Tool 4: render_report — self-contained HTML file
# --------------------------------------------------------------------------- #
def _html_table(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows
    )
    return f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def render_report(title, sections, chart_path=None):
    """Write an HTML report. `sections` is a list of (heading, html) tuples."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    chart_html = ""
    if chart_path:
        chart_html = f'<img src="{os.path.basename(chart_path)}" alt="chart">'
    body = "".join(f"<h2>{h}</h2>{html}" for h, html in sections)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 40px; color: #222; }}
  h1 {{ margin-bottom: 4px; }} .meta {{ color: #777; margin-bottom: 24px; }}
  table {{ border-collapse: collapse; margin: 8px 0 24px; }}
  th, td {{ border: 1px solid #ddd; padding: 6px 12px; text-align: left; }}
  th {{ background: #f5f7fa; }} img {{ max-width: 100%; margin: 12px 0; }}
</style></head>
<body>
  <h1>{title}</h1>
  <div class="meta">Generated {now} · offline reporting agent</div>
  {chart_html}
  {body}
</body></html>"""
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(REPORTS_DIR, f"report_{stamp}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


# --------------------------------------------------------------------------- #
# Tool 5: draft_email — offline "delivery" (writes a .eml file, no network)
# --------------------------------------------------------------------------- #
def draft_email(to, subject, body, attachment=None):
    """Write a standard .eml file you can open/send later. Fully offline."""
    from email.message import EmailMessage

    os.makedirs(REPORTS_DIR, exist_ok=True)
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    if attachment and os.path.exists(attachment):
        with open(attachment, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="html",
                filename=os.path.basename(attachment),
            )
    path = os.path.join(REPORTS_DIR, "draft_email.eml")
    with open(path, "wb") as f:
        f.write(bytes(msg))
    return path


# --------------------------------------------------------------------------- #
# The "agent": parse a plain-English request and decide which tools to run
# --------------------------------------------------------------------------- #
def run_agent(request, rows, columns):
    """Route a request to tools. Understands: report, sum/average/min/max/count,
    'top N <label> by <value>', 'group <value> by <group>', 'chart', 'email to X'.
    """
    req = request.lower().strip()
    out = []          # text lines echoed to the user
    sections = []     # (heading, html) for the report
    chart_pairs = []  # (label, value) pairs for an optional chart
    chart_title = "Chart"

    # --- top N <label> by <value> ---
    m = re.search(r"top\s+(\d+)\s+(.+?)\s+by\s+([\w %$-]+)", req)
    if m:
        n = int(m.group(1))
        label = _resolve_column(m.group(2), columns)
        value = _resolve_column(m.group(3), columns)
        if label and value:
            pairs = top_n(rows, label, value, n)
            chart_pairs, chart_title = pairs, f"Top {n} {label} by {value}"
            out.append(f"Top {n} {label} by {value}:")
            out += [f"  {lbl}: {val:,.2f}" for lbl, val in pairs]
            sections.append(
                (chart_title, _html_table([label, value],
                 [(l, f"{v:,.2f}") for l, v in pairs]))
            )

    # --- group <value> by <group> ---
    m = re.search(r"group\s+([\w %$-]+?)\s+by\s+([\w %$-]+)", req)
    if m:
        value = _resolve_column(m.group(1), columns)
        grp = _resolve_column(m.group(2), columns)
        if value and grp:
            res = group_by(rows, grp, value, "sum")
            pairs = list(res.items())
            if not chart_pairs:
                chart_pairs, chart_title = pairs, f"{value} by {grp}"
            out.append(f"{value} by {grp}:")
            out += [f"  {k}: {v:,.2f}" for k, v in pairs]
            sections.append(
                (f"{value} by {grp}", _html_table([grp, value],
                 [(k, f"{v:,.2f}") for k, v in pairs]))
            )

    # --- single aggregations: sum / average / min / max / count ---
    agg_words = {"sum": "sum", "total": "sum", "average": "mean",
                 "avg": "mean", "mean": "mean", "min": "min",
                 "minimum": "min", "max": "max", "maximum": "max"}
    for word, op in agg_words.items():
        m = re.search(rf"\b{word}\b(?:\s+of)?\s+([\w %$-]+)", req)
        if m:
            col = _resolve_column(m.group(1), columns)
            if col:
                val = aggregate(rows, op, col)
                if val is not None:
                    out.append(f"{op}({col}) = {val:,.2f}")
    if re.search(r"\bcount\b|\bhow many\b", req):
        out.append(f"row count = {len(rows)}")

    # --- full report (default if nothing else matched, or explicitly asked) ---
    wants_report = "report" in req
    if wants_report or not sections and not out:
        s = summarize(rows, columns)
        overview = _html_table(
            ["column", "count", "sum", "mean", "min", "max"],
            [
                (st["column"], st["count"], f"{st['sum']:,.2f}",
                 f"{st['mean']:,.2f}", f"{st['min']:,.2f}", f"{st['max']:,.2f}")
                for st in s["numeric"]
            ],
        )
        sections.insert(0, (f"Overview ({s['rows']} rows)", overview))
        out.append(f"Summarized {s['rows']} rows across {len(s['numeric'])} numeric columns.")
        # default chart: first numeric column, top 10 rows
        if not chart_pairs and s["numeric"]:
            vcol = s["numeric"][0]["column"]
            lcol = columns[0]
            chart_pairs = top_n(rows, lcol, vcol, 10)
            chart_title = f"Top {lcol} by {vcol}"

    # --- chart (build if asked, or if a report is being made) ---
    chart_path = None
    if ("chart" in req or wants_report) and chart_pairs:
        chart_path = make_chart(chart_pairs, chart_title, f"chart_{datetime.now():%H%M%S}.png")
        if chart_path:
            out.append(f"Chart saved -> {chart_path}")
        else:
            out.append("(matplotlib not installed — chart skipped)")

    # --- render the report file if there is anything to show ---
    report_path = None
    if wants_report or "chart" in req:
        report_path = render_report("Data Report", sections or
                                    [("Result", "<p>" + "<br>".join(out) + "</p>")],
                                    chart_path)
        out.append(f"Report saved -> {report_path}")

    # --- email (offline: writes a .eml draft) ---
    m = re.search(r"email\s+(?:to\s+)?([\w.+-]+@[\w.-]+)", req)
    if m:
        to = m.group(1)
        eml = draft_email(to, "Your data report",
                          "\n".join(out), attachment=report_path)
        out.append(f"Email drafted for {to} -> {eml} (offline .eml, open to send)")

    return "\n".join(out) if out else "I couldn't parse that. Try: 'report', " \
        "'sum revenue', 'top 5 product by sales', 'group revenue by region, chart'."


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main():
    if len(sys.argv) < 2:
        print("Usage: python reporting_agent.py <data.csv|xlsx> [request]")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"Error: file not found -> {path}")
        sys.exit(1)

    rows, columns = load_data(path)
    print(f"Loaded {len(rows)} rows, columns: {', '.join(columns)}")

    # one-shot mode
    if len(sys.argv) >= 3:
        print(run_agent(" ".join(sys.argv[2:]), rows, columns))
        return

    # interactive mode
    print("Offline reporting agent ready. Examples:")
    print("  report            top 5 product by revenue")
    print("  sum revenue       group revenue by region, chart")
    print("  email to me@x.com   (writes an offline .eml draft)")
    print("Type 'quit' to exit.\n")
    while True:
        try:
            req = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if req.lower() in {"quit", "exit", "q"}:
            break
        if req:
            print(run_agent(req, rows, columns), "\n")


if __name__ == "__main__":
    main()
