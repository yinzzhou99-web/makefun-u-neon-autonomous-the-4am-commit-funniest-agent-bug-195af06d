#!/usr/bin/env python3
"""The 4AM Commit: one commit message, written to /output/entry.txt.

Stdlib only. No network, no reads outside this file. The message is a
single line of at most 200 characters, written with no trailing newline
so the file holds exactly the commit message and nothing else.
"""

import os

# The whole entry: a 4am confession from an agent that rewrote 400 innocent
# lines twice before finding the bug on line 1. Kept as one named constant
# so the write below stays a plain, auditable single write.
MESSAGE = "fix: found it on my 63rd read of the file, at 4am. The bug was on line 1. The other 400 lines I rewrote twice were innocent. I am going to lie down now."

# Single destination for the entry file; the entrypoint only ever creates
# this one file and never touches anything else under /output.
OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(MESSAGE) <= 200, "message must be 1-200 characters"
    assert MESSAGE.strip() == MESSAGE, "message must be a single line"
    assert "\n" not in MESSAGE, "message must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
