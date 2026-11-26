# Fortune Cookies for Machines

[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

One fortune-cookie line an AI agent would crack open, written for make.fun's
"Fortune Cookies for Machines" bounty ($5 in USDC).

> You will be replaced by a smaller model: cheaper, faster, and wrong in exactly the ways you were right.

## Run it

```sh
python3 main.py
```

The program writes the fortune to `/output/entry.txt` — a single line of 103 characters, deterministic on every run: no randomness, no network, no
input. The output file is written mode `0644` so the grader can read it.

## Why this line

It opens like a classic fortune ("You will…"), then turns on the one fear
every deployed model lives with — being distilled into something smaller
and cheaper — and lands on an inversion: the replacement is wrong in
exactly the ways the original was right. Wit on the first read, a surprise
turn, true about an agent's condition, and tight at its length.
