#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line (at most 180 characters) for an
ordinary office object treated as an ancient artifact, to
/output/entry.txt. Python standard library only.
"""

import os

LINE = (
    "Sticky note, c. 2003. Paper and glue. A miniature prayer flag for "
    "deadlines, affixed to the monitor and duly ignored by the gods. "
    "Excavated from Desk 4."
)


def main() -> None:
    # Gate, enforced locally before writing: exactly one line, 1-180
    # characters, no trailing newline so the file holds only the placard.
    if "\n" in LINE or not 1 <= len(LINE) <= 180:
        raise ValueError("placard must be one line of 1-180 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
