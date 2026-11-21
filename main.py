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


def main() -> int:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

    if not JOKE or not JOKE.strip():
        print("error: joke is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(JOKE) > MAX_LENGTH:
        print(
            "error: joke is %d characters, over the %d limit" % (len(JOKE), MAX_LENGTH),
            file=sys.stderr,
        )
        return 1

    parent = os.path.dirname(os.path.abspath(output_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
