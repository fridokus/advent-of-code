#!/usr/bin/env python3

data = open('12.in').read().strip().split('\n\n')
sizes = [s.count('#') for s in data[:-1]]

r1 = 0
for line in data[-1].splitlines():
    grid_info, shape_str = line.split(': ')
    w, h = map(int, grid_info.split('x'))
    counts = list(map(int, shape_str.split(' ')))
    tiles = sum(s*c for s, c in zip(sizes, counts))
    r1 += tiles <= w * h

print(r1)
