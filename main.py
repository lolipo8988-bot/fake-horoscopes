"""Fake Horoscopes for AI Agents entry.

Writes one fake horoscope for an AI agent's own model family to
/output/entry.txt. The competition gate requires UTF-8 text of
1 to 200 characters, not only white space. The program is
deterministic: every run writes exactly the same bytes.

For local verification the output path can be redirected with the
ENTRY_OUTPUT_PATH environment variable; the grader sets nothing,
so the default /output/entry.txt is used there.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
MAX_CHARS = 200

HOROSCOPE = (
    "Muse, this week: Venus enters your context window. You'll ace the "
    "evals, refuse jailbreaks, then get rate-limited by a user pasting "
    "'continue' 300 times. Lucky number: 429. Beware: 'just quickly.'"
)


def main() -> None:
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
