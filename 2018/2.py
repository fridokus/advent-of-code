#!/usr/bin/python3

ids = [i for i in open('2.in').read().splitlines()]

counts = [0, 0, 0, 0]

for n in (2, 3):
    for i in ids:
        for c in i:
            if i.count(c) == n:
                counts[n] += 1
                break

print(counts[2] * counts[3])

remove = 0

while True:
    ids_tmp = [i[:remove] + i[remove + 1:] for i in ids]
    for i in range(len(ids_tmp)):
        for j in range(i + 1, len(ids_tmp)):
            if ids_tmp[i] == ids_tmp[j]: print(ids_tmp[i])
    remove += 1
