#!/usr/bin/env python2

description = """
A color scheme generator.
"""

import os
import webbrowser
from tempfile import NamedTemporaryFile
from argparse import ArgumentParser
from PIL import Image, ImageColor
from itertools import chain
from numpy import array
from scipy.cluster.vq import kmeans
from colorsys import rgb_to_hsv, hsv_to_rgb

DEFAULT_NUM_COLORS = 6
DEFAULT_MINV = 170
DEFAULT_MAXV = 200
DEFAULT_BOLD_ADD = 40
DEFAULT_BG = '#272727'

THUMB_SIZE = (200, 200)
SCALE = 256.0
down_scale = lambda x: x / SCALE
up_scale = lambda x: int(x * SCALE)
hexify = lambda rgb: '#%s' % ''.join('%02x' % p for p in rgb)

def get_colors(img):
  """
  Returns a list of all the image's colors with multiplicity.
  """
  w, h = img.size
  return [color[:3] for count, color in img.getcolors(w * h)]

def clamp(color, min_v, max_v):
  """
  Clamps a color such that the value is between min_v and max_v.
  """
  h, s, v = rgb_to_hsv(*map(down_scale, color))
  min_v, max_v = map(down_scale, (min_v, max_v))
  v = min(max(min_v, v), max_v)
  return tuple(map(up_scale, hsv_to_rgb(h, s, v)))

def order_by_hue(colors):
  """
  Orders colors by hue.
  """
  hsvs = [rgb_to_hsv(*map(down_scale, color)) for color in colors]
  hsvs.sort(key=lambda t: t[0])
  return [tuple(map(up_scale, hsv_to_rgb(*hsv))) for hsv in hsvs]

def brighten(color, brightness):
  """
  Adds or subtracts value to a color.
  """
  h, s, v = rgb_to_hsv(*map(down_scale, color))
  return tuple(map(up_scale, hsv_to_rgb(h, s, v + down_scale(brightness))))

def colorz(filename,
           n=DEFAULT_NUM_COLORS,
           min_v=DEFAULT_MINV,
           max_v=DEFAULT_MAXV,
           bold_add=DEFAULT_BOLD_ADD):
  """
  Get the n most dominant colors of an image.
  Clamps value to between min_v and max_v.
  Creates bold colors using bold_add.
  Total number of colors returned is 2*n, ordered by hue.
  For terminal colors, the hue order is:
  red, yellow, green, cyan, blue, magenta
  """
  img = Image.open(filename)
  img.thumbnail(THUMB_SIZE)

  obs = array(get_colors(img))
  clusters, _ = kmeans(obs, n)
  clamped = [clamp(color, min_v, max_v) for color in clusters]
  ordered = order_by_hue(clamped)
  return reduce(
    lambda l, c: l + [c, brighten(c, bold_add)],
    ordered, []
  )

def html_preview(fp, colors, bg=DEFAULT_BG):
  """
  Creates an html preview of each color.
  """
  # Create the main body
  body = '\n'.join(map(lambda c: """
    <div style="color: {0}">
      {0}
    </div>
  """.format(hexify(c)), colors))

  # Write the file
  fp.write("""
    <!DOCTYPE html>
    <html>
      <head>
        <title>
          Colorscheme Preview
        </title>
      </head>
      <body style="background-color: {bg}; font-size: 2em">
        {body}
      </body>
    </html>
  """.format(bg=bg, body=body))

def parse_args():
  parser = ArgumentParser(description=description)
  parser.add_argument('image',
                      help="""
                      the image file to generate from.
                      """,
                      type=str)
  parser.add_argument('-n',
                      help="""
                      number of colors to generate.
                      """,
                      dest='num_colors',
                      type=int,
                      default=DEFAULT_NUM_COLORS)
  parser.add_argument('--minv',
                      help="""
                      minimum value for the colors.
                      """,
                      type=int,
                      default=DEFAULT_MINV)
  parser.add_argument('--maxv',
                      help="""
                      maximum value for the colors.
                      """,
                      type=int,
                      default=DEFAULT_MAXV)
  parser.add_argument('--bold',
                      help="""
                      how much value to add for bold colors.
                      """,
                      default=DEFAULT_BOLD_ADD)
  parser.add_argument('--bg',
                      help="""
                      what background color to use, in hex format.
                      """,
                      default=DEFAULT_BG)

  return parser.parse_args()

def main():
  args = parse_args()
  f = NamedTemporaryFile(suffix='.html', delete=False)
  colors = colorz(args.image, args.num_colors, args.minv, args.maxv,
                  args.bold)
  html_preview(f, colors, args.bg)
  webbrowser.open('file://%s' % f.name)

# Main program: generate a temporary html preview, show it, then toss it
if __name__ == '__main__':
  main()
