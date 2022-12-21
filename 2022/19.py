#!/usr/bin/python3

from re import findall
from collections import deque

with open('19.in') as f:
    blueprints = [tuple([l[i+1] for i in range(6)]) for l in [[int(i) for i in findall(r'\d+', line)] for line in f.read().splitlines()]]

def simulate(c, limit):
    s = (0, 1, 0, 0, 0, 0, 0, 0, 0) # time, roots, reources
    visited = set()
    max_ore_c = max(c[:3] + (c[4],))
    ret = 0
    q = deque((s,))
    while q:
        s = q.pop()
        t, ro, re = s[0], list(s[1:5]), list(s[5:])
        ret = max(ret, re[-1])
        if t == limit: continue
        t_left = limit - t
        if ret > re[-1] + t_left * (ro[-1] + sum(range(t_left))): continue
        if t_left * max_ore_c < re[0] + (t_left - 1)*ro[0]: re[0] = t_left * max_ore_c - (t_left - 1)*ro[0]
        if t_left * c[3] < re[1] + (t_left - 1)*ro[1]: re[1] = t_left * c[3] - (t_left - 1)*ro[1]
        if t_left * c[5] < re[2] + (t_left - 1)*ro[2]: re[2] = t_left * c[5] - (t_left - 1)*ro[2]
        if ro[0] > max_ore_c: ro[0] = max_ore_c
        if ro[1] > c[3]: ro[1] = c[3]
        if ro[2] > c[5]: ro[2] = c[5]

        s = (t, *ro, *re)
        if s in visited: continue
        visited |= {s}
        q.append((s[0]+1,) + s[1:5] + tuple([s[i] + s[i+4] for i in range(1, 5)]))
        if re[0] >= c[4] and re[2] >= c[5]:
            q.append((t+1, *ro[:3], ro[3]+1, re[0] - c[4] + ro[0], re[1] + ro[1], re[2] - c[5] + ro[2], re[3] + ro[3]))
        else:
            if re[0] >= c[2] and re[1] >= c[3]: q.append((t+1, *ro[:2], ro[2]+1, ro[3], re[0]-c[2]+ro[0], re[1]-c[3]+ro[1], re[2]+ro[2], re[3]+ro[3]))
            if re[0] >= c[1]: q.append((t+1, ro[0], ro[1]+1, *ro[2:], re[0]-c[1]+ro[0], re[1]+ro[1], re[2]+ro[2], re[3]+ro[3]))
            if re[0] >= c[0]: q.append((t+1, ro[0]+1, *ro[1:], re[0]-c[0]+ro[0], re[1]+ro[1], re[2]+ro[2], re[3]+ro[3]))
    return ret

r1 = 0
r2 = 1
for b, c in enumerate(blueprints):
    if b <3: r2 *= simulate(c, 32)
    r1 += (b+1) * simulate(c, 24)
print(r1)
print(r2)
