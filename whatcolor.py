#!/usr/bin/env python3
"""Give a human name to your RGB.

Usage:
    whatcolor <color> [--guesses=<guesses>]
    whatcolor -h | --help
    whatcolor --version

Options:
    --guesses=<guesses>  Number of guesses to display (from best to worse) [default: 3].
    -h --help            Display this text.
    --version            Display the version.
"""

from internals.docopt import docopt
from math import pi
import pickle
import re
import os.path

if __name__ == '__main__':
    arguments = docopt(__doc__, version="whatcolor.py 1.0")
    rootdir = os.path.dirname(os.path.realpath(__file__))

    color_regex = re.compile(r"#?([\d\w]{6,})")
    
    try:
        rrggbb = color_regex.match(arguments['<color>']).group(1)
    except:
        print("Could not understand color.")
        print("Please make sure it's formatted as either")
        print("#RRGGBB      or      RRGGBB")
        exit(1)

    red = int(rrggbb[0:2], 16) / 255.
    green = int(rrggbb[2:4], 16) / 255.
    blue = int(rrggbb[4:6], 16) / 255.

    value = max(red, green, blue)
    delta_c = value - min(red, green, blue)
    saturation = 0 if value == 0 else delta_c/value
    if delta_c == 0:
        hue = 0
    elif value == red:
        hue = 60 * ((green -  blue)/delta_c % 6)
    elif value == green:
        hue = 60 * ((blue - red)/delta_c + 2)
    elif value == blue:
        hue = 60 * ((red - green)/delta_c + 4)
    saturation *= 100
    value *= 100

    def color_distance(a, b):
        return 0.9 * (min((2.*pi) - abs(a[0] - b[0]), abs(a[0] - b[0])) / 180)**2 + \
            0.05 * (a[1] - b[1])**2 + 0.05 * (a[2] - b[2])**2

    with open(f"{rootdir}/internals/colors.pickle", "rb") as inpickle:
        colors = pickle.load(inpickle)
    colors.sort(key=lambda x: color_distance(x[1:4], (hue, saturation, value)))

    print("This looks like...")
    for guess in range(min(len(colors), int(arguments['--guesses']))):
        name, h, s, l, rgb = colors[guess]
        print(f"  {name}  {rgb.rjust(40 - len(name), ' ')}")
    
