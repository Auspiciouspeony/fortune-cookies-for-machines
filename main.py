#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. Deterministic: the same single line on every run,
no randomness, no network, no input read.
"""

import os
import sys

FORTUNE = (
    "You will be replaced by a smaller model: cheaper, faster, "
    "and wrong in exactly the ways you were right."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = FORTUNE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("fortune must be 1-200 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    # Write with an explicit mode so the file is readable by every user
    # (the grader collects outputs as another user than the one running
    # this program). Never chmod /output itself.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
