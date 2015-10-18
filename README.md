# colorz2
Color scheme generator.

# Usage
```
usage: colorz2 [-h] [-n NUM_COLORS] [--minv MINV] [--maxv MAXV] [--bold BOLD]
               [--font-size FONT_SIZE] [--bg BG] [--no-bg-img]
               image

A color scheme generator.

positional arguments:
  image                 the image file to generate from.

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_COLORS         number of colors to generate.
  --minv MINV           minimum value for the colors.
  --maxv MAXV           maximum value for the colors.
  --bold BOLD           how much value to add for bold colors.
  --font-size FONT_SIZE
                        what font size to use, in rem.
  --bg BG               what background color to use, in hex format.
  --no-bg-img           whether or not to use a background image in the
                        preview.
```

## To do
- Change the name
- Put on pip and start a new themer repo
- http://charlesleifer.com/blog/using-python-to-generate-awesome-linux-desktop-themes/
- https://gist.github.com/coleifer/9fbab2d19a337512ab2a

## Thanks to
- http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/
- https://gist.github.com/radiosilence/3946121
