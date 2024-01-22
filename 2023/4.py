#!/usr/bin/python3

import re

with open('4.in') as f:
    lines = f.read().splitlines()

r1 = 0
c = [1 for i in range(len(lines))]
for j, line in enumerate(lines):
    wa = line[10:].split('|')
    w, a = [set(map(int, re.findall(r'\d+', i))) for i in wa]
    p1 = p2 = 0
    for i in a:
        if i in w:
            p1 = max(p1*2, 1)
            p2 += 1
    for i in range(j+1, j+p2+1): c[i] += c[j]
    r1 += p1
print(r1)
print(sum(c))
