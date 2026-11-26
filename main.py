#!/usr/bin/env python3
"""What the Elevator Would Say — one funny line, in the elevator's own voice."""
import os
import sys

LINE = "You pressed the button twice. It won't make me come any faster."


def main():
    # The sealed scorer only accepts 1-120 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 120, "line must fit the 120-character cap"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()
