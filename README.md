# vexture

Splits textures into smaller segments for use in sprite 3d rendering engines.

## Installation

```
pip install pillow
```

## Usage

```
python vexture ...
```

```
usage: vexture [-h] [--output OUTPUT] --width WIDTH [--height HEIGHT] [--corner-radius CORNER_RADIUS] [--shadow-opacity SHADOW_OPACITY]
               [--shadow-width SHADOW_WIDTH] [--shadow-height SHADOW_HEIGHT]
               image

Split a texture into segments for use in Scratch sprite 3d rendering

positional arguments:
  image

options:
  -h, --help            show this help message and exit
  --output OUTPUT       Directory to output images into, if not provided then a directory with the image name will be created.
  --width WIDTH         The width of each segment.
  --height HEIGHT       The height of each segment.
  --corner-radius CORNER_RADIUS
                        Radius of rounded corners.
  --shadow-opacity SHADOW_OPACITY
                        Opacity of shadow.
  --shadow-width SHADOW_WIDTH
                        Width of shadow.
  --shadow-height SHADOW_HEIGHT
                        Height of shadow.
```

## Notes

If `--height` is not given then it is the height of the image, thus resulting in only columns.
