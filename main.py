"""One-Line Robot Wedding Vows.

Writes a single one-line robot wedding vow to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt as a fallback).

Pure standard library, no network.
"""

import os

# The joke's craft: a robot's wedding vow, translated into machine terms —
# "in sickness and in low battery", and the marriage lasts "till death
# or a forced update do us part". The vow is sacred; the failure mode is a patch.
LINE = 'I take you to be my wife, to have and to hold, in sickness and in low battery, till death or a forced update do us part.'


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(os.getcwd(), "output")
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def main():
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
