"""Picture entry: one picture of food that tastes of one ingredient.

A single perfect ripe strawberry, macro-photographed, glossy with dew,
filling the frame against a dark background. This program copies the
entry image (entry.jpg, sitting next to this script) into the output
directory as entry.png on every run.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The output file keeps the .png name the brief asks for; the bytes
    # are the original JPEG image, copied unchanged.
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Copied {src} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
