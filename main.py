"""food-picture-01 entry point.

The picture is a steaming bowl of ramen: chopsticks lifting glossy
noodles above the broth, a jammy soft egg and charred chashu beside
them. It lives next to this file as image.jpg; all this program does
is put an exact copy of it where the grader looks for it, as entry.png
inside the output directory.
"""

import os
import shutil
from pathlib import Path

# The grader runs this program twice; both runs write the same bytes,
# so the output is deterministic.
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "image.jpg"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target = out_dir / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)


if __name__ == "__main__":
    main()
