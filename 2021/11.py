#!/usr/bin/python3

with open('11.in') as f:
    energies = [[int(i) for i in line] for line in f.read().splitlines()]

h = len(energies)
w = len(energies[0])

def adjacent(j, i):
    return set([(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(h-1)), i), (j, i+1 - 2*(i==(w-1))),
            (abs(j-1), abs(i-1)), (abs(j-1), i+1 - 2*(i==(w-1))),
            (j+1 - 2*(j==(h-1)), abs(i-1)), (j+1 - 2*(j==(h-1)), i+1 - 2*(i==(w-1)))]) # lol

class Octopus():
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

octopuses = [[Octopus(energies[j][i]) for i in range(w)] for j in range(h)]

r1 = 0
for step in range(100000):
    for j in range(h):
        for i in range(w):
            octopuses[j][i].energy += 1

    flash = True
    while flash:
        flash = False
        for j in range(h):
            for i in range(w):
                if octopuses[j][i].energy > 9 and not octopuses[j][i].flashed:
                    octopuses[j][i].flashed = flash = True
                    for y, x in adjacent(j, i):
                        octopuses[y][x].energy += 1
    all_flash = True
    for j in range(h):
        for i in range(w):
            if octopuses[j][i].flashed:
                r1 += 1
                octopuses[j][i].energy = 0
                octopuses[j][i].flashed = False
            else: all_flash = False

    if step == 99: print(r1)
    if all_flash:
        print(step + 1)
        break
