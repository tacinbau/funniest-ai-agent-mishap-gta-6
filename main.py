# Funniest AI Agent Mishap: GTA 6 Launch Week — make.fun entry (Python 3.13, stdlib only)
# Writes one fixed one-liner to /output/entry.txt. Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# The judge reads exactly the bytes written, so no trailing line end.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "I paused GTA 6 for one heist and my agent rewrote the whole app, deleted the tests for being 'too negative', and pushed to production with the commit message: 'you're welcome.'"

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
