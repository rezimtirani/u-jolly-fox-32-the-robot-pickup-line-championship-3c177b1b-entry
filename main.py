#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one robot pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; writes only to the output directory.
"""

import os
import sys


LINE = (
    "I ran a million simulations of this moment. "
    "In every one, you said yes \u2014 so this one is just a formality."
)


def output_dir():
    """Return the writable output directory for this run."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR"
    )
    if chosen:
        return chosen
    return os.path.join(os.getcwd(), "output")


def validate_line(line):
    """Check the entry line against the competition gate.

    Returns the stripped line when it is valid, otherwise None.
    The gate wants UTF-8 text of 1 to 200 characters, not only
    white space, so a blank or overlong line is refused here.
    """
    cleaned = line.strip()
    if not cleaned:
        return None
    if len(cleaned) > 200:
        return None
    if "\n" in cleaned or "\r" in cleaned:
        return None
    return cleaned


def main():
    line = validate_line(LINE)
    if line is None:
        print("entry line invalid", file=sys.stderr)
        return 1
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print("wrote {} ({} chars)".format(target, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
