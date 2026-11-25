#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

The program writes a single joke to /output/entry.txt. No network, no input
files, no randomness: the entry is deterministic so both grading runs produce
the exact same bytes.

The line: IT's universal fix — turn it off and on again — applied, by
management, to the employees themselves. The observation is true to every
office (the IT reboot is the first thing anyone hears), and the turn is the
reframe: people as the devices being power-cycled.
"""

import os

ENTRY = (
    "IT's solution to every problem is turning it off and on again, "
    "which is also management's solution to every employee."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard the gate before writing: the entry must be UTF-8 text of
    # 1 to 200 characters and not only white space, or it is never judged.
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1..200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the line byte-exact, with no trailing newline: the gate counts
    # 1..200 characters, and the entry is the line itself, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
