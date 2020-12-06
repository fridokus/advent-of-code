#!/usr/bin/python3

with open('6.in') as f:
    groups = f.read().split('\n\n')

unions = [set(i.replace('\n', '')) for i in groups]

print(sum([len(i) for i in unions]))

res2 = 0
for i, group in enumerate(groups):
    intersection = unions[i]
    for individual in group.split('\n'):
        intersection = intersection & set([i for i in individual]) if individual else intersection
    res2 += len(intersection)

print(res2)

