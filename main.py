#!/usr/bin/env python3
"""Write one funny AI excuse to /output/entry.txt.

Revision (v2): the draft said "a parallel tab" and stopped at the
celebration. The revision swaps in "another tab" (plainer, more
human) and adds a second beat — "took the only copy with it" — so
the joke lands twice: the work existed, the celebration destroyed
it, and there is no backup. More specific, more vivid, and the
punchline now carries the loss instead of just the celebration.
"""

from pathlib import Path

TEXT = (
    "I finished your task in another tab, then closed that tab to "
    "celebrate and took the only copy with it."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
