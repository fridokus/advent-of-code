#!/usr/bin/python3

with open('10.in') as f:
    lines = f.read().splitlines()

class CRT:
    def __init__(s):
        s.x = 1
        s.cycle = 0
        s.signal_strengths = []
        s.image = [['.']*40 for _ in range(6)]

    def tick(s):
        if s.cycle % 40 in (s.x-1, s.x, s.x+1):
            s.image[s.cycle // 40][s.cycle % 40] = '#'
        s.cycle += 1
        if not (20 + s.cycle) % 40:
            s.signal_strengths.append(s.cycle * s.x)

    def addx(s, x):
        for _ in range(2): s.tick()
        s.x += x

crt = CRT()
for line in lines:
    if line.startswith('no'): crt.tick()
    else: crt.addx(int(line[5:]))

print(sum(crt.signal_strengths))
for l in crt.image: print(''.join(l))
