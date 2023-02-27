import argparse
import shutil
from pathlib import Path

from .image_splitter import image_splitter

argparser = argparse.ArgumentParser(
    prog="vexture",
    description="Split a texture into segments for use in Scratch sprite 3d rendering",
)


def arg_path(argument: str) -> Path:
    path = Path(argument)
    if not path.exists():
        argparser.error(f"{path} does not exist")
    if not path.is_file():
        argparser.error(f"{path} is not a file")
    return path


def arg_dir(argument: str) -> Path:
    path = Path(argument)
    if path.is_file():
        argparser.error(f"{path} exists and is a file")
    return path


argparser.add_argument("image", type=arg_path)
argparser.add_argument(
    "--output",
    type=arg_dir,
    help=(
        "Directory to output images into, "
        "if not provided then a directory with the image name will be created."
    ),
)
argparser.add_argument(
    "--width", type=int, required=True, help="The width of each segment."
)
argparser.add_argument(
    "--height", type=int, help="The height of each segment.", default=None
)
argparser.add_argument(
    "--corner-radius", type=int, default=0, help="Radius of rounded corners."
)
argparser.add_argument(
    "--shadow-opacity", type=int, default=255, help="Opacity of shadow."
)
argparser.add_argument(
    "--shadow-width", type=int, default=None, help="Width of shadow."
)
argparser.add_argument(
    "--shadow-height", type=int, default=16, help="Height of shadow."
)

namespace = argparser.parse_args()
image: Path = namespace.image
output: Path = namespace.output or Path(image.stem)
width: int = namespace.width
height: int | None = namespace.width
corner_radius: int = namespace.corner_radius
shadow_opacity: int = namespace.shadow_opacity
shadow_width: int = namespace.shadow_width or width * 2
shadow_height: int = namespace.shadow_height
shutil.rmtree(output, ignore_errors=True)
output.mkdir()

image_splitter(
    image,
    output,
    width,
    height,
    corner_radius,
    shadow_opacity,
    shadow_width,
    shadow_height,
)
