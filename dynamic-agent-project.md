# Beginner Project: A Dynamic AI Agent (Docs/Excel → reason → Email)

A small **agent** for beginners. Unlike a fixed script, *you* don't hardcode the
steps — you give the model a set of **tools** and let it decide which to call,
in what order, to satisfy your request. You interact through a **CLI** (optional
simple **GUI** later), its data comes from **documents and Excel (.xlsx)**, and
one of its tools **sends email via the Gmail API**.

This doc is the plan. Build it in the order below.

---

## 1. Automation vs. a dynamic agent (the key idea)

| Fixed automation (script)                  | Dynamic agent (this project)                     |
| ------------------------------------------ | ------------------------------------------------ |
| *You* write `read → ask → email` in order  | *Model* chooses which tool to call, and when     |
| `if cmd == "email": send()`                | You say "email John the top sellers"; it plans it |
| Same steps every run                       | Steps depend on the request                      |
| No "reasoning" — just control flow         | Model reasons in a **loop** until the task is done |

The whole trick is a **tool-use loop**: model → picks a tool → your code runs it
→ result goes back to model → repeat → model gives a final answer.

---

## 2. What it does (one sentence)

> Ask in plain English ("read sales.xlsx, find the top 3 products, and email the
> list to sam@example.com") and the agent picks the right tools to do it.

---

## 3. Architecture — the agent loop

```
                        ┌──────────────────────────┐
   your request ──────► │        Gemini            │
                        │  (decides next action)   │
                        └───────┬──────────┬───────┘
                    "call a tool"       "I'm done"
                                │          │
                                ▼          ▼
                    ┌────────────────┐   final answer → you
                    │  YOUR TOOLS    │
                    │  • read_file   │
                    │  • query_data  │
                    │  • send_email  │
                    └───────┬────────┘
                            │  tool result
                            └────────► back into Gemini (loop)
```

The **tools** are just normal Python functions you write. The model never runs
code itself — it *asks* your loop to run a tool, and you send the result back.

Interface to start: **CLI**. (Optional Tkinter GUI later — it calls the same loop.)

---

## 4. Tools & setup

**Python packages**

```bash
pip install google-genai           # Gemini + function calling (you already use this)
pip install python-docx openpyxl   # read .docx and .xlsx
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2  # Gmail
```

**Secrets** — never hardcode (you already do this right in [9.4.py](9.4.py)):

```bash
export GEMINI_API_KEY="your-key-here"
```

**Gmail API** (one-time): Cloud Console → new project → enable **Gmail API** →
create **OAuth client ID** (*Desktop app*) → download `credentials.json`. First
run opens a browser once and saves `token.json`.

> Add `credentials.json` and `token.json` to [.gitignore](.gitignore) — they are secrets.

---

## 5. Build steps (in order)

### Step 1 — Write the tools (plain functions)
These are the *actions* the agent can take. Test each one by calling it directly
before you hand them to the model.

```python
import os, base64
from email.message import EmailMessage

def read_file(path: str) -> str:
    """Read a .txt, .docx, or .xlsx file and return its text."""
    ext = path.lower().rsplit(".", 1)[-1]
    if ext == "txt":
        return open(path, encoding="utf-8", errors="replace").read()
    if ext == "docx":
        from docx import Document
        return "\n".join(p.text for p in Document(path).paragraphs)
    if ext == "xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(path, data_only=True)   # data_only = get values, not formulas
        out = []
        for sheet in wb.worksheets:
            out.append(f"# Sheet: {sheet.title}")
            for row in sheet.iter_rows(values_only=True):
                out.append(", ".join("" if c is None else str(c) for c in row))
        return "\n".join(out)
    return f"Error: unsupported file type .{ext}"

def send_email(to: str, subject: str, body: str) -> str:
    """Send an email via the Gmail API. Returns a status string."""
    service = _gmail_service()          # see helper below
    msg = EmailMessage()
    msg["To"], msg["Subject"] = to, subject
    msg.set_content(body)
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    service.users().messages().send(userId="me", body={"raw": raw}).execute()
    return f"Email sent to {to}"
```

Gmail auth helper (runs the browser login once, then reuses `token.json`):

```python
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def _gmail_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        open("token.json", "w").write(creds.to_json())
    return build("gmail", "v1", credentials=creds)
```

### Step 2 — Register the tools with Gemini
Tell the model what tools exist. With `google-genai` you can pass the Python
functions directly and let it auto-generate the schema from the type hints and
docstrings — so **write clear docstrings**, the model reads them to decide.

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash"

TOOLS = [read_file, send_email]   # the functions from Step 1
```

### Step 3 — The agent loop (the heart of it)
Let the SDK run the loop: it will call your functions, feed results back, and
keep going until the model produces a final text answer.

```python
def run_agent(user_request: str) -> str:
    config = types.GenerateContentConfig(
        tools=TOOLS,
        system_instruction=(
            "You are a helpful data agent. You can read files and send email. "
            "Use read_file before answering questions about a file. "
            "Only send email when the user explicitly asks you to."
        ),
    )
    # automatic_function_calling is ON by default: the SDK runs the loop for you.
    resp = client.models.generate_content(
        model=MODEL, contents=user_request, config=config
    )
    return resp.text
```

> Once this works, try turning **off** automatic function calling and writing the
> loop yourself (check `resp.function_calls`, run them, append results, call
> again). Doing it manually once is the best way to *understand* an agent.

### Step 4 — The interface (CLI first)

```python
def main():
    print("Dynamic agent ready. Try: 'read report.xlsx and summarize it'")
    print("Type 'quit' to exit.\n")
    while True:
        req = input("> ").strip()
        if req.lower() in {"quit", "exit", "q"}:
            break
        if req:
            print(run_agent(req), "\n")

if __name__ == "__main__":
    main()
```

Notice: there is **no** `if "email" in cmd` logic. The model decides when to
read a file and when to send mail. That is what makes it an agent.

Optional **GUI** later: a Tkinter window with a text box and a "Send" button
that calls `run_agent()` — same brain, different front door.

---

## 6. Definition of done (v1 checklist)

- [ ] Three working tools: `read_file` (txt/docx/xlsx) and `send_email` (Gmail).
- [ ] Tools registered with Gemini; model calls them on its own.
- [ ] "Read X and email a summary to Y" works end-to-end from one request.
- [ ] The agent decides the steps — no hardcoded command parsing.
- [ ] `GEMINI_API_KEY` from env; `credentials.json` / `token.json` git-ignored.

---

## 7. Stretch goals (once v1 works)

- Write the tool-use loop **manually** (no auto function calling) to learn it.
- Add a `list_files(folder)` tool so the agent can pick files itself.
- Add memory: keep the conversation history so follow-ups work ("now email that").
- Add a `search_web` tool, or a `.pdf` / `.csv` reader.
- Guardrail: make `send_email` ask for confirmation before sending.
- Build the Tkinter GUI.

---

## 8. Common beginner gotchas

- **Model won't call your tool:** its **docstring** is the instructions it reads —
  make it describe *when* to use the tool and what each argument means.
- **Agent sends email unprompted:** add a rule in `system_instruction` ("only
  email when explicitly asked") and/or a confirmation prompt in the tool.
- **Excel values look wrong:** use `load_workbook(..., data_only=True)`.
- **File too big for the model:** for v1, only read the first ~100 rows / few pages.
- **Gmail "access blocked":** add your account as a *test user* on the OAuth
  consent screen in Cloud Console.
- **Never commit secrets:** re-check `credentials.json`, `token.json`, and keys
  are in `.gitignore`.
