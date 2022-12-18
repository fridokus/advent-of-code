#!/usr/bin/python3

from collections import defaultdict

with open('18.in') as f:
    droplets = {eval('(' + i + ')') for i in f.read().splitlines()}

def adjacent(d):
    yield (d[0] + 1, d[1], d[2])
    yield (d[0] - 1, d[1], d[2])
    yield (d[0], d[1] + 1, d[2])
    yield (d[0], d[1] - 1, d[2])
    yield (d[0], d[1], d[2] + 1)
    yield (d[0], d[1], d[2] - 1)

def calc_area(droplets):
    ret = 0
    for d in droplets:
        for a in adjacent(d):
            if a not in droplets: ret += 1
    return ret
print(calc_area(droplets))

mins = [min((d[i] for d in droplets)) for i in range(3)]
maxs = [max((d[i] for d in droplets)) for i in range(3)]
fill = set()
for d in droplets:
    for a in adjacent(d):
        if a in droplets or a in fill: continue
        potential_fill = {a}
        next_potential_fill = {a}
        while not any([any((d2[i] <= mins[i] for i in range(3))) or any((d2[i] >= maxs[i] for i in range(3))) for d2 in potential_fill]):
            increased = False
            for d2 in potential_fill:
                for a2 in adjacent(d2):
                    if not (a2 in fill or a2 in droplets or a2 in potential_fill or a2 in next_potential_fill):
                        increased = True
                        next_potential_fill |= {a2}
            potential_fill = next_potential_fill.copy()
            if not increased:
                fill |= potential_fill
                break
droplets |= fill
print(calc_area(droplets))
