#!/usr/bin/python3

with open('5.in') as f:
    maps = f.read().split('\n\n')

seeds = [int(i) for i in maps[0][7:].split()]
maps = [[[int(k) for k in j.split()] for j in i.splitlines()[1:]] for i in maps[1:]]

r1 = 100000000000
for n in seeds:
    for m in maps:
        for r in m:
            if r[1] <= n < r[1] + r[2]:
                n += -r[1] + r[0]
                break
    r1 = min(r1, n)
print(r1)

maps = maps[::-1]
seed_ranges = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
for l0 in range(1000000000):
    l = l0
    for m in maps:
        for r in m:
            if r[0] <= l < r[0] + r[2]:
                l += r[1] -r[0]
                break
    for r in seed_ranges:
        if l in r: break
    else: continue
    break
print(l0)
