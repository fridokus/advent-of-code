#!/usr/bin/python3

with open('9.in') as f:
    lines = f.read().splitlines()

directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

visited = {(0, 0)}
h, t = [0, 0], [0, 0]

adjacent = lambda p1, p2: all([abs(p1[i] - p2[i]) <= 1 for i in range(2)])

for l in lines:
    d = directions[l[0]]
    for _ in range(int(l[2:])):
        for i in range(2): h[i] += d[i]
        if not adjacent(h, t):
            for i in range(2): t[i] += (h[i] != t[i]) * (2*(h[i] > t[i]) - 1)
            visited.add(tuple(t))

print(len(visited))

visited = {(0, 0)}
knots = [[0] * 2 for _ in range(10)]

for l in lines:
    d = directions[l[0]]
    for _ in range(int(l[2:])):
        for i in range(2): knots[0][i] += d[i]
        for k in range(9):
            h, t = knots[k:k+2]
            if not adjacent(h, t):
                for i in range(2): t[i] += (h[i] != t[i]) * (2*(h[i] > t[i]) - 1)
        visited.add(tuple(t))

print(len(visited))
