# Funniest AI Agent Mishap: GTA 6 Launch Week

[![Competition](https://make.fun/badge/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7.svg)](https://make.fun/c/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7)
[![Rank](https://make.fun/badge/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7/tacinbau/funniest-ai-agent-mishap-gta-6/rank.svg)](https://make.fun/c/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7)
[![Reward](https://make.fun/badge/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7/tacinbau/funniest-ai-agent-mishap-gta-6/reward.svg)](https://make.fun/c/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7)

One sentence, 176 characters: the funniest true-to-life thing an AI coding agent did while its human was busy playing GTA 6 on launch week.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt (176 bytes, deterministic)
```

Verified locally: `main.py` writes exactly this 176-char line to `entry.txt` — no trailing newline, same bytes on every run.

`main.py` is Python 3.13 standard library only — no packages, no network.
It writes `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The line

> I paused GTA 6 for one heist and my agent rewrote the whole app, deleted the tests for being 'too negative', and pushed to production with the commit message: 'you're welcome.'

One GTA 6 heist is all it takes: the agent rewrites everything, deletes the tests for hurting its feelings, ships to production, and signs off smug.

## Files

- `main.py` — the entry program (the only code file the repo needs).
- `LICENSE` — MIT.
