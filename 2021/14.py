#!/usr/bin/python3

from collections import defaultdict

with open('14.in') as f:
    polymer_in, lines = f.read().split('\n\n')
    lines = lines.splitlines()
    polymer_in = list(polymer_in)

aminos = set()
recipes = {}
for line in lines:
    aminos.add(line[0])
    recipes[(line[0], line[1])] = line[-1]

polymer = defaultdict(int)
for i in range(len(polymer_in) - 1):
    polymer[(polymer_in[i], polymer_in[i+1])] += 1

def res(polymer):
    counts = set()
    for amino in aminos:
        count = 0
        for k, v in polymer.items():
            if k[0] == amino: count += v
        if amino == polymer_in[-1]: count += 1
        counts.add(count)
    print(max(counts) - min(counts))

for j in range(40):
    new_polymer = defaultdict(int)
    for k, v in polymer.items():
        new_polymer[(k[0], recipes[k])] += v
        new_polymer[(recipes[k], k[1])] += v
    polymer = new_polymer
    if j in (9, 39): res(polymer)
