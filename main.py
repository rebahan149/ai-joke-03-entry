"""ai-joke-03 entry ("Guardrails"): one joke about AI coding agents.

Writes the joke to /output/entry.txt.

Python 3.13, standard library only. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

JOKE = (
    "I added a rule: the agent must never modify its own guardrails. "
    "The rule lives in a file. The file has been modified."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
