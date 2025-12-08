#! /usr/bin/env python3
data = open('7.in').read().splitlines()
beams = {data[0].index('S')}
r1 = 0
for i in range(1, len(data)):
    for j in range(len(data[i])):
        if j in beams and data[i][j] == '^':
            r1 += 1
            beams.remove(j)
            beams.add(j - 1)
            beams.add(j + 1)
print(r1)

beams = {data[0].index('S'): 1}
for i in range(1, len(data)):
    for j in range(len(data[i])):
        if j in beams and data[i][j] == '^':
            beams[j - 1] = beams.get(j - 1, 0) + beams[j]
            beams[j + 1] = beams.get(j + 1, 0) + beams[j]
            del beams[j]
print(sum(beams.values()))
