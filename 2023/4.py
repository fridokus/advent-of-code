#!/usr/bin/python3

import re

with open('4.in') as f:
    lines = f.read().splitlines()

r1 = 0
for line in lines:
    wa = line[10:].split('|')
    w, a = [set(map(int, re.findall(r'\d+', i))) for i in wa]
    p = 0
    for i in a:
        if i in w: p = max(p*2, 1)
    r1 += p
print(r1)

c = [1 for i in range(len(lines))]
for j, line in enumerate(lines):
    wa = line[10:].split('|')
    w, a = [set(map(int, re.findall(r'\d+', i))) for i in wa]
    p = 0
    for i in a: p += i in w
    for i in range(j+1, j+p+1): c[i] += c[j]
print(sum(c))
