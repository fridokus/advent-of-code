#!/usr/bin/python3

with open('9.in') as f:
    heightmap = []
    for line in f.read().splitlines():
        heightmap.append([int(i) for i in line])

h = len(heightmap)
w = len(heightmap[0])

def adjacent(j, i):
    return set([(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(h-1)), i), (j, i+1 - 2*(i==(w-1)))])

r1 = 0
low_points = []
for j in range(h):
    for i in range(w):
        if all([heightmap[j][i] < heightmap[y][x] for y, x in adjacent(j, i)]):
            r1 += 1 + heightmap[j][i]
            low_points.append((j, i))

print(r1)

def size(j, i, visited):
    if (j, i) not in visited:
        visited.append((j, i))
        return 1 + sum([size(y, x, visited) if 9 > heightmap[y][x] > heightmap[j][i] else 0 for y, x in adjacent(j, i)])
    else:
        return 0

sizes = []
for p in low_points:
    sizes.append(size(p[0], p[1], []))

sizes = sorted(sizes)[-3:]
print(sizes[0] * sizes[1] * sizes[2])
