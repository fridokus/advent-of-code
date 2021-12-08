#!/usr/bin/python3

with open('7.in') as f:
    crabs = [int(i) for i in f.read().split(',')]

n = len(crabs)

crabs = sorted(crabs)
median = crabs[int(n/2)]
print(sum([abs(i - median) for i in crabs]))

mean = int(sum(crabs) / n)
dists = [abs(i - mean) for i in crabs]
print(sum([i*(i+1)/2 for i in dists]))
