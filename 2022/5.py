#!/usr/bin/python3

import re

with open('5.in') as f:
    stacks1, moves = [i.splitlines() for i in f.read().split('\n\n')]

stacks1 = [[c for c in list(col[-2::-1]) if c != ' '] for col in zip(*stacks1) if col[-1] not in '[ ]']

stacks2 = [[j for j in i ] for i in stacks1]
for move in moves:
    c, f, t = [int(i) for i in re.findall(r'\d+', move)]
    for _ in range(c): stacks1[t-1].append(stacks1[f-1].pop())
    stacks2[t-1] += stacks2[f-1][-c:]
    stacks2[f-1]  = stacks2[f-1][:-c]

print(''.join([stack[-1] for stack in stacks1]))
print(''.join([stack[-1] for stack in stacks2]))
