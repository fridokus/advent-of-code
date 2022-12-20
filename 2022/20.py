#!/usr/bin/python3

with open('20.in') as f:
    ints = [int(i) for i in f.read().splitlines()]

def solve(p2):
    data = {}
    n = len(ints)
    mul = 811589153 if p2 else 1
    for i, v in enumerate(ints): data[i] = [i, v*mul]
    for _ in range(10 if p2 else 1):
        for o in range(n):
            c, v = data[o]
            t = (c + v) % (n-1)
            data[o][0] = t
            for k in range(n):
                if k == o: continue
                if c < data[k][0] <= t or t <= data[k][0] < c:
                    data[k][0] += ((t < c)*2 - 1)
    for k in data:
        if data[k][1] == 0: zero_i = data[k][0]
    ret = 0
    for c in [(zero_i + i) % n for i in (1000, 2000, 3000)]:
        for k in data:
            if data[k][0] == c: ret += data[k][1]
    return ret

print(solve(False))
print(solve(True))
