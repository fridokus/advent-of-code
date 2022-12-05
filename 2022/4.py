#!/usr/bin/python3

import re

with open('4.in') as f:
    assignments = [[int(j) for j in re.findall(r'\d+', i)] for i in f.read().splitlines()]

r1 = r2 = 0
for a in assignments:
    r1 += a[0] >= a[2] and a[1] <= a[3] or a[0] <= a[2] and a[1] >= a[3]
    r2 += bool(set(range(a[0], a[1] + 1)) & set(range(a[2], a[3] + 1)))

print(r1)
print(r2)
