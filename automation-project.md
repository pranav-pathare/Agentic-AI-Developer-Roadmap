# Beginner Automation Project: Read → Summarize → Email

A small, buildable agent for beginners. It reads data from **documents and
Excel (.xlsx)** files, lets you interact through a **CLI** (with an optional
simple **GUI**), and can **share the results over email using the Gmail API**.

This doc is the plan. Build it in the order below — each step works on its own
before you add the next.

---

## 1. What it does (one sentence)

> Point it at a `.docx` / `.txt` / `.xlsx` file, ask it (in plain English) what
> you want, and it can email the answer to someone via Gmail.

Example flow:

```
python automate.py report.xlsx
> summarize the top 5 rows by revenue
> email that to teammate@example.com
```

---

## 2. Scope (keep it small)

| Do this now (v1)                          | Skip for later (v2+)                     |
| ----------------------------------------- | ---------------------------------------- |
| Read `.txt`, `.docx`, `.xlsx`             | PDFs, Google Docs, databases             |
| CLI question/answer loop                  | Web app, auth, multiple users            |
| Send one email via Gmail API              | Attachments, scheduling, HTML templates  |
| Use Gemini to summarize/answer            | Fine-tuning, embeddings, RAG             |
| One optional Tkinter GUI screen           | Fancy UI, packaging into an .exe/.app    |

---

## 3. Architecture (how the pieces fit)

```
              ┌─────────────┐
  file  ───►  │ 1. Loaders  │  read docx / xlsx / txt  →  plain text
              └──────┬──────┘
                     ▼
              ┌─────────────┐
  question ─► │ 2. Agent    │  send text + question to Gemini  →  answer
              └──────┬──────┘
                     ▼
              ┌─────────────┐
  "email it"─►│ 3. Gmail    │  send the answer to a recipient
              └─────────────┘

  Interface (choose one to start):  CLI  ──or──  Tkinter GUI
```

Keep each piece in its own function/file. This matches the style you already
have in [9.4.py](9.4.py).

---

## 4. Tools & setup

**Python packages**

```bash
pip install google-genai           # Gemini (you already use this)
pip install python-docx openpyxl   # read .docx and .xlsx
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2  # Gmail API
```

**API keys / secrets** — never hardcode them (you already do this right):

```bash
export GEMINI_API_KEY="your-key-here"
```

**Gmail API access** (one-time):
1. Go to <https://console.cloud.google.com/> → create a project.
2. Enable the **Gmail API**.
3. Create an **OAuth client ID** (type: *Desktop app*).
4. Download `credentials.json` into the project folder.
5. First run opens a browser to log in; it saves a `token.json` so you only do
   this once.

> Add `credentials.json` and `token.json` to [.gitignore](.gitignore) — they are secrets.

---

## 5. Build steps (in order)

### Step 1 — Read the data sources
Turn each file type into plain text the model can read.

```python
def load_file(path):
    """Return the file's contents as plain text (supports .txt, .docx, .xlsx)."""
    ext = path.lower().rsplit(".", 1)[-1]

    if ext == "txt":
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()

    if ext == "docx":
        from docx import Document
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)

    if ext == "xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(path, data_only=True)
        rows = []
        for sheet in wb.worksheets:
            rows.append(f"# Sheet: {sheet.title}")
            for row in sheet.iter_rows(values_only=True):
                rows.append(", ".join("" if c is None else str(c) for c in row))
        return "\n".join(rows)

    raise ValueError(f"Unsupported file type: .{ext}")
```

**Test it alone:** print the output for one file of each type before moving on.

### Step 2 — Ask the agent (reuse what you have)
This is almost exactly your [9.4.py](9.4.py) `ask()` function — reuse it.

```python
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash"

def ask(file_text, question):
    prompt = (
        "Answer the question using ONLY the data below. "
        "If the answer isn't there, say so.\n\n"
        f"--- DATA ---\n{file_text}\n--- END DATA ---\n\n"
        f"Question: {question}"
    )
    return client.models.generate_content(model=MODEL, contents=prompt).text
```

### Step 3 — Send email via Gmail API
Wrap this in one `send_email()` function so the rest of the code just calls it.

```python
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def _gmail_service():
    creds = None
    import os
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def send_email(to, subject, body):
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    _gmail_service().users().messages().send(userId="me", body={"raw": raw}).execute()
    print(f"Sent to {to}")
```

**Test it alone:** send yourself a hardcoded "hello" email before wiring it up.

### Step 4 — The interface (pick CLI first)

**CLI loop** (start here — simplest):

```python
import sys

def main():
    path = sys.argv[1]
    text = load_file(path)
    last_answer = ""
    print(f"Loaded {path}. Ask a question, or 'email <address>', or 'quit'.")
    while True:
        cmd = input("> ").strip()
        if cmd.lower() in {"quit", "exit", "q"}:
            break
        if cmd.lower().startswith("email "):
            to = cmd.split(" ", 1)[1].strip()
            send_email(to, "Automation result", last_answer or "(nothing yet)")
        elif cmd:
            last_answer = ask(text, cmd)
            print(last_answer, "\n")

if __name__ == "__main__":
    main()
```

**Optional GUI** (Tkinter, ships with Python — no install): one window with a
file picker, a question box, an answer area, and an "Email" button that calls
the same `load_file` / `ask` / `send_email` functions. Only build this after the
CLI works.

---

## 6. Definition of done (v1 checklist)

- [ ] Reads `.txt`, `.docx`, and `.xlsx` and prints their text.
- [ ] Answers a plain-English question about the file using Gemini.
- [ ] Sends that answer to an email address via the Gmail API.
- [ ] `GEMINI_API_KEY` is read from the environment; secrets are in `.gitignore`.
- [ ] Runs end-to-end from the CLI: load → ask → email.

---

## 7. Stretch goals (once v1 works)

- Attach the original file to the email.
- Add a "summarize this whole file" one-command shortcut.
- Support `.pdf` (add `pypdf`) and `.csv`.
- Let a question span **multiple files** in a folder.
- Build the Tkinter GUI.
- Schedule it to run daily (cron / Task Scheduler) and email a report.

---

## 8. Common beginner gotchas

- **Excel gives numbers as text?** Use `data_only=True` (shown above) so you get
  computed values, not formulas.
- **Gmail "access blocked" screen:** add your Google account as a *test user* on
  the OAuth consent screen in Cloud Console.
- **File too big for the model:** for v1, only send the first ~100 rows / a few
  pages. Chunking is a v2 concern.
- **Don't commit secrets:** double-check `credentials.json`, `token.json`, and
  any key are ignored by git.
