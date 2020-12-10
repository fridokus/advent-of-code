#!/usr/bin/python3

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

i = 0
res2 = 1
while i < len(diffs):
    ones_in_a_row = 0
    while diffs[i] == 1:
        ones_in_a_row += 1
        i += 1
    res2 *= factors[ones_in_a_row]
    i += 1

print(res2)
