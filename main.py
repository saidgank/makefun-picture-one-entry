"""One picture of food that tastes of one ingredient.

A single perfect ripe strawberry, macro-photographed, glossy with dew,
filling the frame against a dark background. This program copies the
entry image (entry.jpg) sitting next to it into the output directory
as entry.png, every run.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # One ingredient, one picture: the strawberry is the whole entry.
    print(f"Copied {src} -> {dst}")


if __name__ == "__main__":
    main()
