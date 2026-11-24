#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (101 characters, within the
140-character gate) for the invented city Presswick to /output/entry.txt.

Line: In Presswick, a warm wind irons your shirt as you walk to work,
so you arrive looking like you tried.
"""

import os
from pathlib import Path

LINE = (
    "In Presswick, a warm wind irons your shirt as you walk to work, "
    "so you arrive looking like you tried."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
