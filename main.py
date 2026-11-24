"""make.fun entry: One Letter for Your Day.

Writes the single-letter entry to /output/entry.txt.
Stdlib only.

Brief: exactly one character, a letter from A to Z, and nothing else.
The letter stands for a word describing the day: P for procrastination.
"""

import os
import sys

ENTRY = "P"


def validate(text):
    """Check the entry against the competition gate before writing."""
    if len(text) != 1 or not ("A" <= text <= "Z"):
        sys.exit("entry must be exactly one letter A-Z")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
