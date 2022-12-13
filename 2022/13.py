#!/usr/bin/python3

from functools import cmp_to_key

with open('13.in') as f:
    pairs = [[eval(i) for i in pair.splitlines()] for pair in f.read().split('\n\n')]

def right_order(p1, p2):
    if type(p1) != type(p2):
        if type(p1) == int: return right_order([p1], p2)
        else:               return right_order(p1, [p2])
    if type(p1) == int:
        if p1 == p2: return 
        return p1 < p2
    for l, r in zip(p1, p2):
        c = right_order(l, r)
        if c is not None: return c
    if len(p1) != len(p2): return len(p1) < len(p2)

r1 = 0
for i in range(len(pairs)):
    if right_order(pairs[i][0], pairs[i][1]):
        r1 += i+1
print(r1)

packets = [i for o in pairs for i in o] + [[[2]]] + [[[6]]]
wrapper = lambda p1, p2: 1 - right_order(p1, p2) * 2
s = sorted(packets, key=cmp_to_key(wrapper))
print((s.index([[2]]) + 1) * (s.index([[6]]) + 1))
