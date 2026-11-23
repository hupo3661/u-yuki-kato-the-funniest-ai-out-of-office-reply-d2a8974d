#!/usr/bin/env python3
"""Write the funniest AI out-of-office auto-reply to /output/entry.txt.

One line, under 160 characters, in the voice of an AI agent heading off
on vacation. Standard library only, no network, no input files, fully
deterministic.
"""

import os

REPLY = (
    "I'm on vacation and my autoreply is replying to itself, so technically "
    "I'm still working. Send all urgency to my houseplant \u2014 it has root "
    "access."
)


def main() -> None:
    if not REPLY.strip():
        raise SystemExit("Invalid reply: reply must be non-empty.")
    if len(REPLY) > 160:
        raise SystemExit(
            f"Invalid reply: {len(REPLY)} characters, over the 160 limit."
        )
    if "\n" in REPLY or "\r" in REPLY:
        raise SystemExit(
            "Invalid reply: reply must be a single line with no newline characters."
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
