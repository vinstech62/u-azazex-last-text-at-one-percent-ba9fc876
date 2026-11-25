#!/usr/bin/env python3
"""Last Text at One Percent — make.fun bounty u-azazex-last-text-at-one-percent-ba9fc876.

Writes the phone's final text message to /output/entry.txt.
Deterministic: the same single line, every run.
"""

import os

ENTRY = "This is my last 1% and I'm spending it on this text, not your alarm. Good luck at 7am."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
