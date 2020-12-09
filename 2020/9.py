#!/usr/bin/python3

with open('9.in') as f:
    v = [int(i) for i in f.read().splitlines()]

for i in range(25, len(v)):
    if not v[i] in {x + y for x in v[i-25:i] for y in v[i-25:i] if x != y}: break

print(v[i])

for j in range(len(v), 0, -1):
    k = j - 2
    while sum(v[k:j]) < v[i]: k -= 1
    if sum(v[k:j]) == v[i]: break

print(max(v[k:j]) + min(v[k:j]))
