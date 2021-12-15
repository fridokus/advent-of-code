#!/usr/bin/python3

from collections import defaultdict

def res(grid):
    size = len(grid)
    goal = (size-1, size-1)

    adjacent = lambda j, i: {(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(size-1)), i), (j, i+1 - 2*(i==(size-1)))}

    visited = set()
    d = defaultdict(set)
    d[0].add((0, 0))

    for cost in range(100000):
        for p in d[cost]:
            if p == goal: return cost
            for a in adjacent(p[0], p[1]):
                if a in visited: continue
                visited.add(a)
                d[cost + grid[a[0]][a[1]]].add(a)

with open('15.in') as f:
    grid = [[int(i) for i in line] for line in f.read().splitlines()]

print(res(grid))

size = len(grid)
new_grid = [[0 for i in range(size*5)] for j in range(size*5)]

for y in range(5):
    for x in range(5):
        for j in range(size):
            for i in range(size):
                new_grid[y*size + j][x*size + i] = (grid[j][i] + y + x - 1) % 9 + 1

print(res(new_grid))
