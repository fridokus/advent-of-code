#! /usr/bin/env python3
import functools

lines = open('11.in').read().splitlines()

d = dict()
for line in lines:
    d[line[:3]] = line[5:].split(' ')

@functools.cache
def paths(current, target):
    if current == target:
        return 1
    if current not in d:
        return 0

    r = 0
    for o in d[current]:
        r += paths(o, target)
    return r

r1 = paths('you', 'out')
print(r1)

# only one path will be valid since acyclic
r2 = paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out')
print(r2)
