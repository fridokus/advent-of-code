#!/usr/bin/python3

from re          import findall
from collections import defaultdict
from functools   import cmp_to_key

with open('15.in') as f:
    readings = [[int(i) for i in findall(r'-?\d+', line)] for line in f.read().splitlines()]

cmp = lambda l1, l2: (l1[0] > l2[0]) * 2 - 1
readings = sorted(readings, key=cmp_to_key(cmp))

xmaxes = defaultdict(int)
r1min, r1max = 0, 0
for r in readings:
    d = abs(r[0] - r[2]) + abs(r[1] - r[3])
    for y in range(r[1] - d, r[1] + d+1):
        dx = d - abs(y - r[1])
        xmin, xmax = r[0] - dx, r[0] + dx + 1
        if xmin <= xmaxes[y] < xmax: xmaxes[y] = xmax
        if y == 2_000_000: r1min, r1max = min(r1min, xmin), max(r1max, xmax)

print(r1max - r1min - 1)
for k in range(4_000_000):
    if 0 <= xmaxes[k] <= 4_000_000: break
print(k + xmaxes[k] * 4_000_000)
