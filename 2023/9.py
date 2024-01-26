#!/usr/bin/python3

with open('9.in') as f:
    lines = f.read().splitlines()

lines = [[int(i) for i in line.split()] for line in lines]
r1 = r2 = 0
for line in lines:
    h = [line]
    while any([h[-1][i] != 0 for i in range(len(h[-1]))]):
        h.append([h[-1][i+1] - h[-1][i] for i in range(len(h[-1]) - 1)])
    r1 += sum([h[i][-1] for i in range(len(h))])
    r2 += sum([h[i][0] * (1 - 2*(i%2)) for i in range(len(h))])
print(r1)
print(r2)
