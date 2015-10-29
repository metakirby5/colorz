# colorz2
Color scheme generator.

![Shinobu and Miku](https://u.teknik.io/SkxEfz.png)

![Miku and Sonico](https://u.teknik.io/OICaW1.png)

# Dependencies
- Python 2
- Pillow
- Numpy
- Scipy

# Usage
```
usage: colorz2 [-h] [-n NUM_COLORS] [--minv MINV] [--maxv MAXV] [--bold BOLD]
               [--font-size FONT_SIZE] [--bg-color BG_COLOR] [--no-bg-img]
               [--no-preview]
               image

A color scheme generator. Takes an image (local or online) and grabs the most
dominant colors using kmeans. Also creates bold colors by adding value to the
dominant colors. Finally, outputs the colors to stdout (one normal and one
bold per line, space delmited) and generates an HTML preview of the color
scheme.

positional arguments:
  image                 the image file or url to generate from.

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_COLORS         number of colors to generate (excluding bold).
                        Default: 6
  --minv MINV           minimum value for the colors. Default: 170
  --maxv MAXV           maximum value for the colors. Default: 200
  --bold BOLD           how much value to add for bold colors. Default: 40
  --font-size FONT_SIZE
                        what font size to use, in rem. Default: 1
  --bg-color BG_COLOR   what background color to use, in hex format. Default:
                        #272727
  --no-bg-img           whether or not to use a background image in the
                        preview. Default: background image on
  --no-preview          whether or not to generate and show the preview.
                        Default: preview on
```

## To do
- Custom implementation of kmeans - repel from bgc,
attract to default term colors
- Change the name
- Put on pip and start a new themer repo
- http://charlesleifer.com/blog/using-python-to-generate-awesome-linux-desktop-themes/
- https://gist.github.com/coleifer/9fbab2d19a337512ab2a

## Thanks to
- http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/
- https://gist.github.com/radiosilence/3946121
