#!/usr/bin/python3

from itertools import combinations
import numpy as np

class Moon():
    def __init__(self, coords):
        self.coords = coords
        self.velo = [0, 0, 0]

    def apply_velo(self):
        for i in range(3):
            self.coords[i] += self.velo[i]

    @property
    def energy(self):
        return sum([abs(i) for i in self.coords]) * sum([abs(i) for i in self.velo])

class System():
    def __init__(self, coords_list):
        self.moons = []
        for coords in coords_list:
            self.moons.append(Moon(coords))

    def update_velocities(self):
        for moon_pair in combinations(self.moons, 2):
            diffs = [moon_pair[1].coords[i] - moon_pair[0].coords[i] for i in range(3)]
            for i in range(3):
                if diffs[i] > 0:
                    moon_pair[0].velo[i] += 1
                    moon_pair[1].velo[i] -= 1
                elif diffs[i] < 0:
                    moon_pair[0].velo[i] -= 1
                    moon_pair[1].velo[i] += 1

    def update_positions(self):
        for moon in self.moons:
            moon.apply_velo()

    def step(self):
        self.update_velocities()
        self.update_positions()

    @property
    def energy(self):
        return sum([moon.energy for moon in self.moons])


coords_list = [
        [15, -2, -6],
        [-5, -4, -11],
        [0, -6, 0],
        [5, 9, 6]
        ]

# system = System(coords_list)

# for i in range(1000):
#     system.step()

# print(system.energy)

# b

system = System(coords_list)
loop_intervals = [0 for i in range(3)]

step_counter = 0
while not all(loop_intervals):
    system.step()
    step_counter += 1
    for l in range(3):
        if loop_intervals[l]:
            continue
        velo_this_dimension = tuple((moon.velo[l] for moon in system.moons))
        if velo_this_dimension == (0, 0, 0, 0):
            loop_intervals[l] = step_counter * 2

print(loop_intervals)
print(np.lcm.reduce(loop_intervals))
