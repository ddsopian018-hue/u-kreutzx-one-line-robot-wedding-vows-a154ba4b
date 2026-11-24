"""One-Line Robot Wedding Vows entry for make.fun competition
u-kreutzx-one-line-robot-wedding-vows-a154ba4b.

Writes one line of wedding vows for a robot couple to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).

Pure Python stdlib, deterministic, no network, no reads outside the repo.
The program refuses to emit anything outside 1-160 characters or anything
that is not exactly one line.
"""

import os
import sys

# The vow works because it IS the classic wedding vow, with the machine
# swapped in at exactly the two load-bearing words: "health" becomes
# "low battery", and the closing "till death do us part" is interrupted
# by "or a forced update". The laugh lands in the last few words, and
# the joke would not work for a human couple.
VOW = (
    "I take you to be my wife, to have and to hold, in sickness and in "
    "low battery, till death or a forced update do us part."
)

MAX_CHARS = 160


def main():
    text = VOW.strip()

    if not 1 <= len(text) <= MAX_CHARS:
        print(
            "Refusing to emit: vow is %d chars, must be 1-%d."
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    if not text:
        print("Refusing to emit: vow is empty or only whitespace.", file=sys.stderr)
        return 1

    if "\n" in text or "\r" in text:
        print("Refusing to emit: vow is not exactly one line.", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Read back what was written and re-check it: the file the grader
    # sees must decode as UTF-8 and hold exactly one non-blank line.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        emitted = f.read()
    lines = emitted.split("\n")
    if len(lines) != 2 or lines[1] != "" or not lines[0].strip():
        print("Refusing to emit: written file failed its own check.", file=sys.stderr)
        return 1
    if lines[0] != text:
        print("Refusing to emit: written text does not match the vow.", file=sys.stderr)
        return 1

    print("Wrote %s (%d chars, one line)." % (out_path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
