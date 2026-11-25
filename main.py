#!/usr/bin/env python3
"""Write the one-line office joke to /output/entry.txt.

Stdlib only, deterministic, no network. One fixed line: the meeting
that could have been an email spawns follow-up meetings, a shared doc
and a working group to decide what the email should have said.
"""
import os
from pathlib import Path

LINE = (
    "The meeting that could have been an email has spawned three "
    "follow-up meetings, a shared doc, and a working group to decide "
    "what the email should have said."
)

MAX_CHARS = 200


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "line must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
