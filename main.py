"""One picture of food that tastes of one ingredient.

A single perfect ripe strawberry, macro-photographed, glossy with dew,
filling the frame against a dark background. This program copies the
entry picture (entry.jpg, sitting next to this file) into the output
directory as entry.png on every run.
"""

import os
import shutil


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.jpg")
    destination = os.path.join(output_dir, "entry.png")
    # The picture is one ingredient only: one strawberry, nothing else.
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
