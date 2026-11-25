#!/usr/bin/env python3
"""Charm the Commuter v2 — forecast for the invented city Tatterwick.

Writes one 100-character forecast line to /output/entry.txt (or to
$OUTPUT_DIR/entry.txt when that variable is set). The file holds the
line exactly, with no trailing newline, so the gate counts 100 chars.

Line: In Tatterwick, rain falls only on people carrying umbrellas,
so nobody in the city owns one anymore.
"""

import os

ENTRY_TEXT = (
    "In Tatterwick, rain falls only on people carrying umbrellas, "
    "so nobody in the city owns one anymore."
)

OUTPUT_NAME = "entry.txt"


def entry_path() -> str:
    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, OUTPUT_NAME)


def main() -> None:
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
