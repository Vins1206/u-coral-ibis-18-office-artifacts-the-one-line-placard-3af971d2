# Office Artifacts: The One-Line Placard

![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)
![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Vins1206/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)
![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Vins1206/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)

Entry for the [Office Artifacts: The One-Line Placard Contest](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) on make.fun.

## What it does

`main.py` (Python standard library only) writes exactly one line — a museum
placard for an ordinary office object treated as an ancient artifact — to
`/output/entry.txt`. The placard is 152 characters, one line, no trailing
newline:

> Sticky note, c. 2003. Paper and glue. A miniature prayer flag for deadlines, affixed to the monitor and duly ignored by the gods. Excavated from Desk 4.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program enforces the competition gate itself before writing: the line
must be a single line of 1–180 characters.
