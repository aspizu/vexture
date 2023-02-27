from pathlib import Path

from PIL import Image

from .create_svg import create_svg


def image_splitter(
    image_path: Path,
    output_dir: Path,
    width: int,
    height: int | None,
    corner_radius: int,
    shadow_opacity: int,
    shadow_width: int,
    shadow_height: int,
):
    image = Image.open(image_path)
    height = height or image.height
    for i, x in enumerate(range(0, image.width, width)):
        for j, y in enumerate(range(0, image.height, height)):
            with (output_dir / f"{image_path.stem}_{i}_{j}.svg").open("w") as svg_file:
                segment = image.crop((x, y, x + width, y + height))
                create_svg(
                    svg_file,
                    segment,
                    corner_radius,
                    shadow_opacity,
                    shadow_width,
                    shadow_height,
                )
    Path("tmp.png").unlink()
