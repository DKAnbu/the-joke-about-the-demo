"""Write a one-line joke about an AI coding agent crashing during a live demo.

The program writes exactly one line of text to the output file named by the
ENTRY_OUTPUT environment variable (default /output/entry.txt). The text is
UTF-8, a single line, 1-280 Unicode code points, and not only whitespace.
Standard library only; no network access.
"""

import os
import sys

JOKE = (
    "My agent demoed the feature it built, crashed in front of fifty people, "
    "apologised, and rebuilt the exact same bug \u2014 with better comments this time."
)

MAX_LENGTH = 280


def validate(text: str) -> str | None:
    """Return the reason the joke is invalid, or None when it is fine."""
    if not text or not text.strip():
        return "empty-or-whitespace"
    if "\n" in text or "\r" in text:
        return "not-single-line"
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        return "control-character"
    if len(text) > MAX_LENGTH:
        return "over-limit-%d-of-%d" % (len(text), MAX_LENGTH)
    return None


def main() -> int:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

    problem = validate(JOKE)
    if problem is not None:
        print("error: joke invalid (%s)" % problem, file=sys.stderr)
        return 1

    parent = os.path.dirname(os.path.abspath(output_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
