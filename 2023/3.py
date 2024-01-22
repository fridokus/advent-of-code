#!/usr/bin/python3

import re
from collections import defaultdict
from functools import reduce

with open('3.in') as f:
    lines = f.read().splitlines()

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
h = len(lines) - 1
w = len(lines[0]) - 1
adjacent = lambda x, y: {(abs(x-1), abs(y-1)), (abs(x-1), y), (abs(x-1), min(y+1, h)), (x, abs(y-1)), (x, min(y+1, h)), (min(x+1, w), abs(y-1)), (min(x+1, w), y), (min(x+1, w), min(y+1, h))}

gears = defaultdict(set)

r1 = 0
for y, line in enumerate(lines):
    for m in re.finditer(r'\d+', line):
        part = False
        for x in range(m.start(), m.end()):
            for i, j in adjacent(x, y):
                if lines[j][i] not in digits and lines[j][i] != '.':
                    part = True
                    if lines[j][i] == '*':
                        gears[(i, j)] |= {int(m.group())}
        r1 += int(m.group()) * part
print(r1)

r2 = 0
for gear in gears:
    if len(gears[gear]) == 2:
        r2 += reduce(lambda x, y: x*y, gears[gear])
print(r2)
