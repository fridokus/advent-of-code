#!/usr/bin/python3

import itertools
import functools

with open('10.in') as f:
    v = sorted([0] + [int(i) for i in f.read().splitlines()])
    v += [max(v) + 3]

diffs = [v[i] - v[i-1] for i in range(1, len(v))]
print(sum([i == 3 for i in diffs]) * sum([i == 1 for i in diffs]))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

factors = [1] + [sum(fib(i)) for i in range(10)][2:]
factors_for_all_stretches = [factors[len([j for j in i if j == 1])] for _, i in itertools.groupby(diffs)]
print(functools.reduce(lambda i, j: i * j, factors_for_all_stretches))
