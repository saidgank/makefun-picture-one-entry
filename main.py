"""One picture of food that tastes of one ingredient.

A single perfect ripe strawberry, macro-photographed, glossy with dew,
filling the frame against a dark background. This program copies the
entry image (entry.jpg, sitting next to this script) into the output
directory as entry.png on every run.
"""

import os
import shutil
import sys


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.jpg")
    destination = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(source):
        print(f"entry image not found: {source}", file=sys.stderr)
        sys.exit(1)

    # The output is always named entry.png, regardless of the source name,
    # so the judge always finds the picture at the same path.
    shutil.copyfile(source, destination)
    print(f"Copied {source} -> {destination}")


if __name__ == "__main__":
    main()
