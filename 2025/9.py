#! /usr/bin/env python3

from itertools import combinations

data = open('9.in').read().splitlines()
p = {(x, y) for x, y in [map(int, line.split(',')) for line in data]}
r1 = 0

for p1, p2 in combinations(p, 2):
    r1 = max(r1, (abs(p1[0]-p2[0]) + 1) * (abs(p1[1]-p2[1]) + 1))

print(r1)
p = [(x, y) for x, y in [map(int, line.split(',')) for line in data]]
if p[0] != p[-1]:
    p.append(p[0])

r2 = 0

edges_h = []
edges_v = []
for k in range(len(p)-1):
    x3, y3 = p[k]
    x4, y4 = p[k+1]
    if y3 == y4:
        edges_h.append((y3, min(x3, x4), max(x3, x4)))
    else:
        edges_v.append((x3, min(y3, y4), max(y3, y4)))

for i in range(len(p)-1):
    for j in range(i+1, len(p)-1):
        x1, y1 = p[i]
        x2, y2 = p[j]

        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        for vx, v_y1, v_y2 in edges_v:
            if min_x < vx < max_x and not (v_y2 <= min_y or v_y1 >= max_y):
                break
        else:
            for hy, h_x1, h_x2 in edges_h:
                if min_y < hy < max_y and not (h_x2 <= min_x or h_x1 >= max_x):
                    break
            else:
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                r2 = max(r2, area)

print(r2)
