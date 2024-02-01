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
    if m[p] == 'S': return [(p[0]+1, p[1]), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0], p[1]-1)][::-1] # 🤣
    return set()

d = defaultdict(set)
for j, i in product(range(h), range(w)):
    if m[(j, i)] == 'S':
        d[0] = {(j, i)}
        v = {(j, i)}
        break

c = set()
for i in range(h*w):
    for p in d[i]:
        for a in adjacent(p):
            if a not in d[i-1] and p in adjacent(a):
                d[i+1] |= {a}
                v |= {a}
                if   a[0] - p[0] == -1: c |= {(p[0], p[1] + 1)} | {(a[0], a[1] + 1)}
                elif a[0] - p[0] ==  1: c |= {(p[0], p[1] - 1)} | {(a[0], a[1] - 1)}
                elif a[1] - p[1] == -1: c |= {(p[0] - 1, p[1])} | {(a[0] - 1, a[1])}
                elif a[1] - p[1] ==  1: c |= {(p[0] + 1, p[1])} | {(a[0] + 1, a[1])}
                break
    if d[0] == d[i+1]: break
print((i+1) // 2)

c -= v
adjacent = lambda p: {(p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)}
while True:
    c2 = set()
    for p in c:
        c2 |= {p}
        for a in adjacent(p):
            if a not in v: c2 |= {a}
    if c == c2: break
    c = c2
print(len(c))
