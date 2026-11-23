"""Entry writer for make-the-ai-judge-feel-curious-20261122-2311.

Writes one short, calm, intriguing text to the output file.
Deterministic, standard library only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "She kept the spare key under the stone by the door, "
    "though no one ever visited. "
    "One evening she lifted the stone and found a second key beside it, "
    "bright and new, that fit no lock in the house."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
