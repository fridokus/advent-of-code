#! /usr/bin/env python3

lines = open('11.in').read().splitlines()

d = dict()
for line in lines:
    d[line[:3]] = line[5:].split(' ')

memo = {}
def paths(current, target):
    if (current, target) in memo:
        return memo[(current, target)]

    if current == target:
        return 1
    if current not in d:
        return 0

    r = 0
    for o in d[current]:
        r += paths(o, target)

    memo[(current, target)] = r
    return r

r1 = paths('you', 'out')
print(r1)

r2 = paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out')
print(r2)
