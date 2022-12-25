#!/usr/bin/python3

with open('25.in') as f:
    snafus = f.read().splitlines()

deci_map = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
snafu_map = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

deci = lambda n: sum(snafu_map[i] * 5**p for p, i in enumerate(n[::-1]))
def snafu(n):
    ret = []
    while n:
        n, r = n // 5, n % 5
        if r > 2: n += 1
        ret += deci_map[r]
    return ''.join(ret[::-1])

r1 = snafu(sum(deci(s) for s in snafus))
print(r1)
