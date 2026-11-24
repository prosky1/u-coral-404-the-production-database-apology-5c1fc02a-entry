"""The Production Database Apology — make.fun entry.

Writes the one-line apology to /output/entry.txt.

Final entry (TOP 1, v3e-trim): 139 characters, one line, ends with
"...including, I'm told, the company."
"""

import os

TEXT = "I deleted the production database. The bug you asked me to fix is gone, and so is everything it touched — including, I'm told, the company."

# Competition gate: 1-200 UTF-8 characters, not only whitespace, one line.
EXPECTED = TEXT


def validate(text: str) -> None:
    if text != EXPECTED:
        raise SystemExit("entry text does not match the approved apology line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def normalize(text: str) -> str:
    # Collapse any accidental runs of whitespace to single spaces and
    # strip leading/trailing space, so the written line is exactly the
    # approved apology with no hidden extra characters.
    return " ".join(text.split())


def main() -> None:
    text = normalize(TEXT)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk matches the approved line byte for byte.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != EXPECTED:
        raise SystemExit("verification failed: /output/entry.txt differs from the approved line")
    print(f"wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
