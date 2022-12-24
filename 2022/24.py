#!/usr/bin/python3

with open('24.in') as f:
    scan = f.read().splitlines()

h = len(scan)
w = len(scan[0])
walls = {(1, -1), (w-2, h)}
blizzards = set()
for j in range(h):
    for i in range(w):
        if scan[j][i] == '#':   walls |= {(i, j)}
        elif scan[j][i] == '^': blizzards |= {(i, j,  0, -1)}
        elif scan[j][i] == 'v': blizzards |= {(i, j,  0,  1)}
        elif scan[j][i] == '>': blizzards |= {(i, j,  1,  0)}
        elif scan[j][i] == '<': blizzards |= {(i, j, -1,  0)}

pos = {(1, 0)}
adjacent = lambda x, y: ((x, y), (x-1, y), (x+1, y), (x, y+1), (x, y-1))
done1 = done2 = False
for ro in range(1, 20000):
    blizzards = {(b[0] + b[2], b[1] + b[3], b[2], b[3]) for b in blizzards}
    blizzards2 = set()
    for b in blizzards:
        if   b[0] == 0:   blizzards2 |= {(w-2, b[1], b[2], b[3])}
        elif b[0] == w-1: blizzards2 |= {(1, b[1], b[2], b[3])}
        elif b[1] == 0:   blizzards2 |= {(b[0], h-2, b[2], b[3])}
        elif b[1] == h-1: blizzards2 |= {(b[0], 1, b[2], b[3])}
        else:             blizzards2 |= {b}
    blizzards = blizzards2.copy()
    b_pos = {(b[0], b[1]) for b in blizzards}
    pos2 = set()
    for p in pos:
        for a in adjacent(*p):
            if a in walls or a in b_pos: continue
            pos2 |= {a}
    pos = pos2.copy()
    if not done1 and not done2 and (w-2, h-1) in pos:
        print(ro)
        done1 = pos = {(w-2, h-1)}
    elif done1 and not done2 and (1, 0) in pos: done2 = pos = {(1, 0)}
    elif done1 and done2 and (w-2, h-1) in pos: break
print(ro)
