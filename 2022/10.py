#!/usr/bin/python3

with open('10.in') as f:
    lines = f.read().splitlines()

class CRT:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal_strengths = []
        self.image = [['.']*40 for _ in range(6)]

    def tick(self):
        if self.cycle % 40 in (self.x-1, self.x, self.x+1):
            self.image[self.cycle // 40][self.cycle % 40] = '#'
        self.cycle += 1
        if not (20 + self.cycle) % 40:
            self.signal_strengths.append(self.cycle * self.x)

    def addx(self, x):
        for _ in range(2): self.tick()
        self.x += x

crt = CRT()
for line in lines:
    if line.startswith('no'): crt.tick()
    else: crt.addx(int(line[5:]))

print(sum(crt.signal_strengths))
for l in crt.image: print(''.join(l))
