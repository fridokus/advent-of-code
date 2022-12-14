#!/usr/bin/python3

from itertools import product

with open('14.in') as f:
    lines = f.read().splitlines()

rocks = set()
abyss = 0
for line in lines:
    points = [eval('(' + i + ')') for i in line.split(' -> ')]
    for i in range(len(points) - 1):
        minx, maxx = min(points[i][0], points[i+1][0]), max(points[i][0], points[i+1][0])
        miny, maxy = min(points[i][1], points[i+1][1]), max(points[i][1], points[i+1][1])
        abyss = max(maxy, abyss)
        for x, y in product(range(minx, maxx+1), range(miny, maxy+1)):
            rocks |= {(x, y)}

def move_once(s, rocks):
    if   (s[0],   s[1]+1) not in rocks: s[0], s[1] = s[0],   s[1]+1
    elif (s[0]-1, s[1]+1) not in rocks: s[0], s[1] = s[0]-1, s[1]+1
    elif (s[0]+1, s[1]+1) not in rocks: s[0], s[1] = s[0]+1, s[1]+1
    else: return 
    return True

for i in range(1000): rocks |= {(i, abyss+2)}
n_rocks = len(rocks)
r1 = 0
while True == True:
    s = [500, 0]
    while move_once(s, rocks): pass
    if s[1] >= abyss and not r1:
        print(r1 := len(rocks) - n_rocks)
    rocks |= {tuple(s)}
    if not s[1]: break
print(len(rocks) - n_rocks)
