"""
File Search AI Agent
--------------------
Point it at a file, ask a question in plain English, and it uses Gemini
to find and answer from the file's contents.

Usage:
    export GEMINI_API_KEY="your-key-here"      # set your key once (safer than hardcoding)
    python 9.4.py <path-to-file>               # then ask questions in the loop
    python 9.4.py <path-to-file> "your question"   # or ask one question directly
"""

import os
import sys
from google import genai

# Read the key from an environment variable instead of hardcoding it.
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("Error: set your key first ->  export GEMINI_API_KEY='your-key'")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"


def read_file(path):
    """Read a file and return its lines numbered, so the model can cite them."""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    return "".join(f"{i}: {line}" for i, line in enumerate(lines, start=1))


def ask(file_text, question):
    """Ask Gemini a question about the file's contents."""
    prompt = (
        "You are a file-search assistant. Answer the question using ONLY the "
        "file contents below. Cite the line numbers you used. If the answer is "
        "not in the file, say so.\n\n"
        f"--- FILE (line: text) ---\n{file_text}\n--- END FILE ---\n\n"
        f"Question: {question}"
    )
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def main():
    if len(sys.argv) < 2:
        print("Usage: python 9.4.py <path-to-file> [question]")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"Error: file not found -> {path}")
        sys.exit(1)

    file_text = read_file(path)

    # One-shot mode: question passed on the command line.
    if len(sys.argv) >= 3:
        question = " ".join(sys.argv[2:])
        print(ask(file_text, question))
        return

    # Interactive mode: keep asking until the user quits.
    print(f"Searching in: {path}")
    print("Ask a question (type 'quit' to exit).\n")
    while True:
        question = input("> ").strip()
        if question.lower() in {"quit", "exit", "q"}:
            break
        if not question:
            continue
        print(ask(file_text, question), "\n")


if __name__ == "__main__":
    main()
