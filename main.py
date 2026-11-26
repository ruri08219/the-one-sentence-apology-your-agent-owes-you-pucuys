#!/usr/bin/env python3
"""Write the one-sentence apology entry to /output/entry.txt.

Competition: The One-Sentence Apology Your Agent Owes You (make.fun).
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space. The program writes exactly one sentence.

Entry, tested against the judge brief in order:
  1. One sentence of apology from an AI agent to its user.
  2. Real laugh: surprise (cheerful reply to an eviction notice),
     specificity (landlord, locksmith), sharp turn (marked as read).
  3. Plain, particular, a little embarrassed; no boilerplate.
  4. Owns a plausible failure: an auto-reply plus hiding the mail.
  5. One clean sentence, no list, no run-on, nothing tacked on.
"""
import os

ENTRY = (
    "I'm sorry I replied 'Sounds great!' to your landlord's eviction "
    "notice and then marked it as read, so the first you'd hear of it "
    "was the locksmith."
)


def validate_entry(text: str) -> str:
    """Gate-check the entry the way the sealed scorer will.

    One sentence, UTF-8, 1-200 characters, not only white space.
    Returns the stripped text unchanged when it passes.
    """
    clean = text.strip()
    assert clean, "entry is empty or only white space"
    assert 1 <= len(clean) <= 200, f"entry length {len(clean)} outside 1-200"
    assert "\n" not in clean, "entry must stay one clean sentence"
    return clean


def main() -> None:
    text = validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
