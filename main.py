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


def validate_reply(reply: object) -> None:
    """Explicitly validate the reply text, exiting with a clear error."""
    if not isinstance(reply, str):
        raise SystemExit(
            f"Invalid reply: reply must be a string, got {type(reply).__name__}."
        )
    if not reply.strip():
        raise SystemExit("Invalid reply: reply must be non-empty.")
    if len(reply) > 160:
        raise SystemExit(
            f"Invalid reply: {len(reply)} characters, over the 160 limit."
        )
    if "\n" in reply or "\r" in reply:
        raise SystemExit(
            "Invalid reply: reply must be a single line with no newline characters."
        )


def main() -> None:
    validate_reply(REPLY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not isinstance(out_dir, str) or not out_dir.strip():
        raise SystemExit(
            "Invalid output directory: MAKEFUN_OUTPUT_DIR must be a "
            "non-empty path."
        )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        written = f.write(REPLY)
    if written != len(REPLY):
        raise SystemExit(
            f"Failed to write reply: wrote {written} of {len(REPLY)} characters "
            f"to {path}."
        )
    with open(path, encoding="utf-8") as f:
        saved = f.read()
    if not saved.strip():
        raise SystemExit(f"Invalid output: {path} is empty after writing.")
    if saved != REPLY:
        raise SystemExit(
            f"Invalid output: contents of {path} do not match the validated reply."
        )


if __name__ == "__main__":
    main()
