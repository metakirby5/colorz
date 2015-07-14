from PIL import Image, ImageColor
from itertools import chain
from numpy import array
from scipy.cluster.vq import kmeans
from colorsys import rgb_to_hsv, hsv_to_rgb

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

def colorz(filename, n=6, min_v=170, max_v=200, bold_add=40):
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

def html_preview(filename, colors, bg='#272727'):
  """
  Creates an html preview of each color.
  """
  with open(filename, 'w') as f:

    # Create the main body
    body = '\n'.join(map(lambda c: """
      <div style="color: {0}">
        {0}
      </div>
    """.format(hexify(c)), colors))

    # Write the file
    f.write("""
      <body style="background-color: {bg}; font-size: 2em">
        {body}
      </body>
    """.format(bg=bg, body=body))

