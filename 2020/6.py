#!/usr/bin/python3
import functools

with open('6.in') as f:
    groups = f.read().split('\n\n')

print(sum([len(i) for i in [set(i.replace('\n', '')) for i in groups]]))
print(sum([len(functools.reduce(set.intersection, [set(list(i)) for i in group.split('\n') if i])) for group in groups]))
