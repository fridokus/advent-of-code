#!/usr/bin/python3

from itertools import product, combinations

with open('11.in') as f:
    u = f.read().splitlines()

transpose = lambda x: list(zip(*x))
for _ in range(2):
    u0 = []
    for line in u:
        for _ in range(1 + all([i == '.' for i in line])):
            u0.append(line)
    u = transpose(u0)

gs = set()
for j, i in product(range(len(u)), range(len(u[0]))):
    if u[j][i] == '#':
        gs |= {(j, i)}

r1 = 0
for g1, g2 in combinations(gs, 2):
    r1 += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(r1)

with open('t11.in') as f:
    u = f.read().splitlines()

e = []
for _ in range(2):
    u0 = []
    e.append([])
    for j, line in enumerate(u):
        if all([i == '.' for i in line]):
            e[-1].append(j)
    u = transpose(u0)

print(e)
