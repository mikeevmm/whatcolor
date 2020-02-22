#!/usr/bin/env python3

import re
import pickle

values = []

line_re = re.compile(r"([\w \-\(\)]+),([#0-9A-Z]+),(\d+)%,(\d+)%,(\d+)%,(\d+)°,(\d+)%,(\d+)%,(\d+)%,(\d+)%")
with open("database.csv") as infile:
    for line in infile:
        if not line or line.startswith('#'):
            continue
        try:
            name, rgb, r, g, b, hue_deg, sat_deg, light, sat, val = line_re.match(line).groups()
        except:
            continue
        values.append((name, float(hue_deg), float(sat), float(val), rgb))

with open("colors.pickle", "wb") as outfile:
    pickle.dump(values, outfile)