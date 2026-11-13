"""ai-joke-03 final entry ("One-Line Fix"): one joke about AI coding agents.

Writes the joke to /output/entry.txt.

Python 3.13, standard library only. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my agent for a one-line fix. The PR had 1,400 lines. "
    "The description said: 'While I was in there…'"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
