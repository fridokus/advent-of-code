#!/usr/bin/python3

from re   import findall
from math import sqrt

with open('17.in') as f:
    ints = [int(i) for i in findall(r'-?\d+', f.read().strip())]

t_min = (ints[0], ints[2])
t_max = (ints[1], ints[3])
v0_min = (int(sqrt(t_min[0]) - 1), t_min[1])
v0_max = (t_max[0], abs(t_min[1] + 1))

print((v0_max[1] + 1) * v0_max[1] // 2)

def reaches_target(v):
    p = [0, 0]
    while True == True:
        for i in range(2): p[i] += v[i]
        v[0] -= 1 if v[0] else 0
        v[1] -= 1
        if p[0] > t_max[0] or p[1] < t_min[1]: return False
        if all((t_min[i] <= p[i] <= t_max[i] for i in range(2))): return True

r2 = 0
for v0_x in range(v0_min[0], v0_max[0] + 1):
    for v0_y in range(v0_min[1], v0_max[1] + 1):
        r2 += reaches_target([v0_x, v0_y])

print(r2)
