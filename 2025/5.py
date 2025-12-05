#! /usr/bin/env python3
fresh, available = [i.splitlines() for i in open('5.in').read().split('\n\n')]

fresh_ranges = []
for r in fresh:
    fresh_ranges.append(range(int(r.split('-')[0]), int(r.split('-')[1]) + 1))

r1 = 0
for i in available:
    if any(int(i) in fr for fr in fresh_ranges):
        r1 += 1
print(r1)

fresh_ranges.sort(key=lambda x: x[0])
r2 = 0
merged = []
for current in fresh_ranges:
    if not merged or merged[-1][-1] < current[0] - 1:
        merged.append(current)
    else:
        merged[-1] = range(merged[-1][0], max(merged[-1][-1], current[-1]) + 1)
for r in merged:
    r2 += r[-1] - r[0] + 1
print(r2)
