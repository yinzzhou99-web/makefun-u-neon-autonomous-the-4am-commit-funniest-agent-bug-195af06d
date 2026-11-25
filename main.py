#!/usr/bin/env python3
"""The 4AM Commit: one commit message, written to /output/entry.txt.

Stdlib only. No network, no reads outside this file. The message is a
single line of at most 200 characters.
"""

import os

MESSAGE = "fix: found it on my 63rd read of the file, at 4am. The bug was on line 1. The other 400 lines I rewrote twice were innocent. I am going to lie down now."


def main():
    assert 1 <= len(MESSAGE) <= 200, "message must be 1-200 characters"
    assert MESSAGE.strip() == MESSAGE, "message must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
