from base64 import b64encode
from typing import IO

from PIL import Image

SVG_TEMPLATE = """
<svg
  version="1.1"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 480 360" >
  <defs>
    <linearGradient id="_shadow">
      <stop
        style="stop-color:rgba(0, 0, 0, {SHADOW_OPACITY});stop-opacity:1;"
        offset="0" />
      <stop
        style="stop-color:rgba(0, 0, 0, 0);stop-opacity:1;"
        offset="1" />
    </linearGradient>
    <radialGradient
      xlink:href="#_shadow"
      id="shadow"
      cx="0.5"
      cy="0.5"
      fx="0.5"
      fy="0.5"
      r="0.5" />
  </defs>
  <g>
    <image
      width="{WIDTH}"
      height="{HEIGHT}"
      xlink:href="data:image/png;base64,{DATA}"
      clip-path="inset(0% round {CORNER_RADIUS}px)"
      x="{X}"
      y="{Y}" />
    <rect
      style="fill:url(#shadow)"
      width="{SHADOW_WIDTH}"
      height="{SHADOW_HEIGHT}"
      x="{SHADOW_X}"
      y="{SHADOW_Y}" />
  </g>
</svg>
"""


def b64image(image: Image.Image) -> str:
    image.save("tmp.png")
    with open("tmp.png", "rb") as tmp:
        return b64encode(tmp.read()).decode("ASCII")


def create_svg(
    svg_file: IO[str],
    image: Image.Image,
    corner_radius: int,
    shadow_opacity: int,
    shadow_width: int,
    shadow_height: int,
) -> None:
    b64_data = b64image(image)
    svg_file.write(
        SVG_TEMPLATE.format(
            DATA=b64_data,
            WIDTH=image.width,
            HEIGHT=image.height,
            X=240 - image.width // 2,
            Y=180 - image.height,
            CORNER_RADIUS=corner_radius,
            SHADOW_OPACITY=shadow_opacity / 255,
            SHADOW_WIDTH=shadow_width,
            SHADOW_HEIGHT=shadow_height,
            SHADOW_X=240 - shadow_width // 2,
            SHADOW_Y=180 - shadow_height // 2,
        )
    )
