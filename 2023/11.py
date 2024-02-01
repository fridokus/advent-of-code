#!/usr/bin/python3

from itertools import product, combinations

with open('11.in') as f:
    u = f.read().splitlines()

transpose = lambda x: list(zip(*x))

e = []
for _ in range(2):
    u0 = []
    e.append([])
    for j, line in enumerate(u):
        u0.append(line)
        if all([i == '.' for i in line]): e[-1].append(j)
    u = transpose(u0)

gs = set()
for j, i in product(range(len(u)), range(len(u[0]))):
    if u[j][i] == '#':
        gs |= {(j, i)}

r1 = r2 = 0
for g1, g2 in combinations(gs, 2):
    y2, y1 = max(g1[0], g2[0]), min(g1[0], g2[0])
    x2, x1 = max(g1[1], g2[1]), min(g1[1], g2[1])
    c1 = sum([y1 < e[0][i] < y2 for i in range(len(e[0]))])
    c2 = sum([x1 < e[1][i] < x2 for i in range(len(e[1]))])
    r1 += (y2 - y1) + c1 + (x2 - x1) + c2
    r2 += (y2 - y1) + 999999*c1 + (x2 - x1) + 999999*c2
print(r1)
print(r2)
