#!/usr/bin/python3

from itertools import product
from collections import defaultdict

with open('10.in') as f:
    lines = f.read().splitlines()

h, w = len(lines), len(lines[0])
m = {(j, i): lines[j][i] for j, i in product(range(h), range(w))}

def adjacent(p):
    if p[0] < 0 or p[1] < 0 or p[0] == h or p[1] == w: return set()
    if m[p] == '|': return {(p[0]-1, p[1]), (p[0]+1, p[1])}
    if m[p] == '-': return {(p[0], p[1]-1), (p[0], p[1]+1)}
    if m[p] == 'L': return {(p[0]-1, p[1]), (p[0], p[1]+1)}
    if m[p] == 'J': return {(p[0]-1, p[1]), (p[0], p[1]-1)}
    if m[p] == '7': return {(p[0]+1, p[1]), (p[0], p[1]-1)}
    if m[p] == 'F': return {(p[0]+1, p[1]), (p[0], p[1]+1)}
    if m[p] == 'S': return {(p[0]+1, p[1]), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0], p[1]-1)}
    return set()

d = defaultdict(set)
for j, i in product(range(h), range(w)):
    if m[(j, i)] == 'S':
        d[0] = {(j, i)}
        visited = {(j, i)}
        break

for i in range(h*w):
    for p in d[i]:
        for a in adjacent(p):
            if a not in d[i-1] and p in adjacent(a):
                d[i+1] |= {a}
                visited |= {a}
    if not d[i+1]: break
print(i)

for j, i in product(range(h), range(w)):
    p = (j, i)
