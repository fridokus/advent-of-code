#!/usr/bin/python3

with open('6.in') as f:
    fishes = [int(i) for i in f.read().split(',')]

counts = [fishes.count(i) for i in range(9)]

def loop(counts, n):
    for _ in range(n):
        counts.append(counts[0])
        counts[7] += counts[0]
        counts = counts[1:]
    return counts

counts = loop(counts, 80)
print(sum(counts))

counts = loop(counts, 256 - 80)
print(sum(counts))
