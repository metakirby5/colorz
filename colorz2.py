from PIL import Image, ImageColor
from itertools import chain
from numpy import array
from scipy.cluster.vq import kmeans
from colorsys import rgb_to_hsv, hsv_to_rgb

THUMB_SIZE = (200, 200)
COLORS = [ImageColor.getrgb(s) for s in [
  'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
]]
SCALE = 256.0
down_scale = lambda x: x / SCALE
up_scale = lambda x: int(x * SCALE)
hexify = lambda rgb: '#%s' % ''.join('%02x' % p for p in rgb)

def get_colors(img):
  """
  Returns a list of all the image's colors with multiplicity.
  """
  w, h = img.size
  return list(chain(*(
    [color] * count
    for count, color in img.getcolors(w * h)
  )))

def normalize(color, min_v=0, max_v=256):
  print color
  h, s, v = rgb_to_hsv(*map(down_scale, color))
  min_v, max_v = map(down_scale, (min_v, max_v))
  v = min(max(min_v, v), max_v)
  print "%s %s %s" % (h, s, v)
  return tuple(map(up_scale, hsv_to_rgb(h, s, v)))

def colorz(filename, min_v=80, max_v=160):
  """
  Get the dominant colors of an image, using the terminal colors
  as guesses. Normalizes value to between min_v and max_v.
  """
  img = Image.open(filename)
  img.thumbnail(THUMB_SIZE)

  obs = array(get_colors(img))
  guess = array(COLORS)
  clusters, _ = kmeans(obs, guess)
  return [normalize(color, min_v, max_v) for color in clusters]
