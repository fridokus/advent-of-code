#!/usr/bin/python3

from itertools import product

with open('12.in') as f:
    lines = f.read().splitlines()

mt = [[ord(i) for i in line] for line in lines]
h = len(mt)
w = len(mt[0])
for y, x in product(range(h), range(w)):
    if mt[y][x] == ord('S'):
        mt[y][x] = ord('a')
        start = {(x, y)}
    elif mt[y][x] == ord('E'):
        mt[y][x] = ord('z')
        target = (x, y)

def adjacent(p):
    return [(min(p[0]+1, w-1), p[1]), (max(0, p[0]-1), p[1]), (p[0], min(p[1]+1, h-1)), (p[0], max(0, p[1]-1))]

def hike(new_pos):
    visited = new_pos.copy()
    for i in range(h*w):
        if target in visited: return i
        old_pos = new_pos.copy()
        new_pos = set()
        for p in old_pos:
            for a in adjacent(p):
                if a in visited: continue
                if mt[a[1]][a[0]] > mt[p[1]][p[0]] + 1: continue
                new_pos |= {a}
        visited |= new_pos

print(hike(start))

start = set()
for y, x in product(range(h), range(w)):
    if mt[y][x] == ord('a'): start |= {(x, y)}
print(hike(start))
