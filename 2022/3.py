#!/usr/bin/python3

with open('3.in') as f:
    rs = f.read().splitlines()

r1 = 0
for r in rs:
    c = set.pop(set(r[:len(r)//2]) & set(r[len(r)//2:]))
    r1 += ord(c) - 96 if c.islower() else ord(c) - 38

print(r1)

r2 = 0
for i in range(0, int(len(rs)), 3):
    b = set.pop(set(rs[i]) & set(rs[i+1]) & set(rs[i+2]))
    r2 += ord(b) - 96 if b.islower() else ord(b) - 38

print(r2)
