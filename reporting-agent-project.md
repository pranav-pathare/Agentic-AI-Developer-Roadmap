# Project Plan: A Reporting Agent (Data → Analyze → Report → Deliver)

An **agent** that automates reporting. You point it at data (CSV / Excel / docs),
ask in plain English for the report you want, and it decides how to pull the
numbers, write the summary, render a report, and deliver it (save a file and/or
email it). Same **tool-use loop** idea as [dynamic-agent-project.md](dynamic-agent-project.md) —
Gemini reasons and picks tools; your Python functions do the work.

This doc is the plan. Build it in the order below.

---

## 1. What it does (one sentence)

> "Read `sales.xlsx`, summarize this month's revenue vs. last month, make a
> report with a chart, and email it to sam@example.com" — and the agent plans
> and runs every step itself.

---

## 2. Why an agent (not a fixed script)

| Fixed report script                     | Reporting **agent** (this project)              |
| --------------------------------------- | ----------------------------------------------- |
| One report, hardcoded columns/layout    | You describe the report in words each time      |
| Breaks when the ask changes             | Model re-plans: different metric, filter, format |
| You wire read → compute → format → send | Model chooses which tools to call, and when      |

The whole trick is the **tool-use loop**: model → picks a tool → your code runs
it → result goes back → repeat → model produces the final report.

---

## 3. Architecture — the agent loop

```
   "report on Q3 sales, email it"
              │
              ▼
     ┌──────────────────┐   "call a tool"    ┌──────────────────────┐
     │      Gemini       │ ─────────────────► │  YOUR TOOLS          │
     │ (decides next     │                    │  • load_data         │
     │  action)          │ ◄───────────────── │  • run_analysis      │
     └────────┬─────────┘   tool result       │  • make_chart        │
              │ "I'm done"                     │  • render_report     │
              ▼                                │  • send_email        │
     final report → you / inbox                └──────────────────────┘
```

Interface to start: **CLI**. Every tool is a plain Python function with a clear
docstring — the model reads the docstring to decide when to call it.

---

## 4. Tools & setup

**Python packages**

```bash
pip install google-genai                 # Gemini + function calling
pip install pandas openpyxl              # read/analyze CSV & Excel
pip install matplotlib                    # charts
pip install jinja2                        # HTML report template
# optional: pip install weasyprint       # HTML → PDF
# email reuses the Gmail setup from dynamic-agent-project.md
```

**Secrets** — from env, never hardcoded (as in [9.4.py](9.4.py)):

```bash
export GEMINI_API_KEY="your-key-here"
```

**Gmail** (optional, for the email tool): reuse Section 4 of
[dynamic-agent-project.md](dynamic-agent-project.md) — enable Gmail API, download
`credentials.json`, and keep `credentials.json` / `token.json` in
[.gitignore](.gitignore). Also git-ignore generated `reports/` output.

---

## 5. The tools (what the agent can do)

Write and test each one **directly** before handing it to the model.

1. **`load_data(path)`** → load CSV/XLSX into a DataFrame; return a compact
   preview (shape, column names, dtypes, first rows) as text for the model.
2. **`run_analysis(path, question)`** → the workhorse: aggregate/filter/compare
   (e.g. group by month, sum revenue, top-N, % change). Return the numbers as a
   small table/dict — small enough to fit in the model's context.
3. **`make_chart(path, kind, x, y, title)`** → save a matplotlib PNG to
   `reports/` and return the file path.
4. **`render_report(title, summary, tables, chart_paths)`** → fill a Jinja2 HTML
   template; return the saved report path. (Stretch: also export PDF.)
5. **`send_email(to, subject, body, attachments)`** → Gmail send with the report
   attached. Reuse the helper from the dynamic-agent doc. **Guardrail:** only
   send when the user explicitly asks.

> Keep tool *outputs small*. Return summaries and file paths, not entire
> datasets — that's what keeps the loop cheap and reliable.

---

## 6. Build steps (in order)

1. **Data in.** Write `load_data` + `run_analysis`. Test on a real CSV/XLSX by
   calling them directly. Confirm the numbers are right before anything else.
2. **Register tools with Gemini.** Pass the functions to
   `types.GenerateContentConfig(tools=[...])`; the SDK auto-generates schemas
   from type hints + docstrings, so write clear docstrings.
3. **Agent loop.** Start with **automatic function calling** (on by default), a
   good `system_instruction` ("read/analyze before reporting; only email when
   asked"), and one `generate_content` call. Verify the model chains the tools.
4. **Reporting output.** Add `make_chart` + `render_report` so a run produces an
   actual HTML report file in `reports/`.
5. **Delivery.** Add `send_email` with the confirm-before-send guardrail.
6. **CLI.** A `while True` prompt loop (like [9.4.py](9.4.py)) that calls
   `run_agent(request)`. No `if "email" in cmd` parsing — the model decides.

---

## 7. Definition of done (v1)

- [ ] `load_data` + `run_analysis` return correct numbers from a real file.
- [ ] Tools registered; the model calls them on its own (no hardcoded steps).
- [ ] "Analyze X and build a report" produces an HTML report with a chart.
- [ ] "…and email it to Y" attaches and sends via Gmail, only when asked.
- [ ] Secrets from env; `credentials.json` / `token.json` / `reports/` git-ignored.

---

## 8. Stretch goals

- **Scheduling:** run daily/weekly via `cron` (mac/Linux) so reports auto-send.
- **Manual loop:** turn off auto function calling and write the loop yourself
  (inspect `resp.function_calls`, run them, feed results back) to learn it.
- **More sources:** add `.pdf` / Google Sheets / a SQL `query_db` tool.
- **Memory:** keep history so "now compare it to last quarter" works.
- **PDF export** with WeasyPrint; **Slack** delivery as an alternative to email.
- **Confirmation UX:** show the report path and ask before sending.

---

## 9. Common gotchas

- **Model won't call a tool:** its **docstring** is the spec — say *when* to use
  it and what each argument means.
- **Too much data in context:** return summaries + file paths, not raw rows.
- **Excel values wrong:** `load_workbook(..., data_only=True)` / `pandas.read_excel`.
- **Agent emails unprompted:** enforce "only when asked" in `system_instruction`
  *and* a confirm step in `send_email`.
- **Wrong numbers:** unit-test `run_analysis` directly — the model trusts whatever
  it returns.
