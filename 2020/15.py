#!/usr/bin/python3

with open('15.in') as f:
    line = f.read().split(',')

v = {int(v): k for k, v in enumerate(line[:-1])}

last_spoken = line[-1]
for t in range(len(v), 30000000):
    last_added = last_spoken
    try:
        last_spoken = t - 1 - v[last_spoken]
        v[last_added] = t - 1
    except KeyError:
        v[last_spoken] = t - 1
        last_spoken = 0
    if t == 2019: print(last_spoken)

print(last_spoken)
