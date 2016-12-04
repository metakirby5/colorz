========
 colorz
========

|Sample Usage|

Color scheme generator.

Installation
------------

::

   pip install colorz

or just move ``colorz.py`` to somewhere in your ``$PATH``.
If you do the latter, you must install the dependencies in the
following section manually.

Dependencies
------------

- Python (2 or 3)
- Pillow
- scipy

Usage
-----

::

  usage: colorz [-h] [-n NUM_COLORS] [--minv MINV] [--maxv MAXV] [--bold BOLD]
                [--font-size FONT_SIZE] [--bg-color BG_COLOR] [--no-bg-img]
                [--no-preview]
                image

  A color scheme generator. Takes an image (local or online) and grabs the most
  dominant colors using kmeans. Also creates bold colors by adding value to the
  dominant colors. Finally, outputs the colors to stdout (one normal and one
  bold per line, space delimited) and generates an HTML preview of the color
  scheme.

  positional arguments:
    image                 the image file or url to generate from.

  optional arguments:
    -h, --help            show this help message and exit
    -n NUM_COLORS         number of colors to generate (excluding bold).
                          Default: 6
    --minv MINV           minimum value for the colors. Default: 170
    --maxv MAXV           maximum value for the colors. Default: 200
    --bold BOLD           how much value to add for bold colors. Default: 50
    --font-size FONT_SIZE
                          what font size to use, in rem. Default: 1
    --bg-color BG_COLOR   what background color to use, in hex format. Default:
                          #272727
    --no-bg-img           whether or not to use a background image in the
                          preview. Default: background image on
    --no-preview          whether or not to generate and show the preview.
                          Default: preview on

Thanks to
---------

- http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/
- https://gist.github.com/radiosilence/3946121

.. |Sample Usage| image:: http://i.imgur.com/QVLSXqK.png
   :target: colorz.png
   :alt: Color preview.
