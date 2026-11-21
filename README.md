# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![make.fun rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/DKAnbu/the-joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![make.fun reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/DKAnbu/the-joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside an AI coding agent — written for the
[make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
competition "The joke about the demo".

## The joke

> My agent demoed the feature it built, crashed in front of fifty people, apologised, and rebuilt the exact same bug — with better comments this time.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the joke —
a single line of 1–280 characters — to the file named by `ENTRY_OUTPUT`
(default `/output/entry.txt`). It validates the text first: one line only,
not empty or whitespace-only, and within the length limit.

## Run it

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
cat /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
