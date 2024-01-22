#!/usr/bin/python3

import re

with open('2.in') as f:
    lines = f.read().splitlines()

r1 = 0
r2 = 0
for line in lines:
    i = int(re.search(r'\d+', line).group())
    possible = True
    rmax = gmax = bmax = 0
    for s in line[7:].split(';'):
        r = g = b = 0
        for c in s.split(','):
            if 'red' in c:    r = int(re.findall(r'\d+', c)[0])
            elif 'blue' in c: b = int(re.findall(r'\d+', c)[0])
            else:             g = int(re.findall(r'\d+', c)[0])
        rmax = max(r, rmax)
        gmax = max(g, gmax)
        bmax = max(b, bmax)
        if r > 12 or g > 13 or b > 14: possible = False
    r1 += possible * i
    r2 += rmax * gmax * bmax
print(r1)
print(r2)
