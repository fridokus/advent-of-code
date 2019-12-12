#!/usr/bin/python3

from itertools import combinations

def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = 54
num2 = 24

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

coords_list = [
        [-1, 0, 2],
        [2, -10, -7],
        [4, -8, 8],
        [3, 5, -1]
        ]

# system = System(coords_list)

# for i in range(1000):
#     system.step()

# print(system.energy)

# b

system = System(coords_list)

loop_intervals = [0 for i in range(3)]
points_visited_per_dimension = [[] for i in range(3)]
velos_visited_per_dimension = [[] for i in range(3)]

for i in range(3):
    coords_this_dimension = tuple((moon.coords[i] for moon in system.moons))
    velo_this_dimension = tuple((moon.velo[i] for moon in system.moons))
    points_visited_per_dimension[i].append(coords_this_dimension)
    velos_visited_per_dimension[i].append(velo_this_dimension)

print(points_visited_per_dimension)
print(velos_visited_per_dimension)

step_counter = 0
while not all(loop_intervals):
    system.step()
    step_counter += 1
    for i in range(3):
        if loop_intervals[i]:
            continue
        coords_this_dimension = tuple((moon.coords[i] for moon in system.moons))
        velo_this_dimension = tuple((moon.velo[i] for moon in system.moons))
        if (coords_this_dimension in points_visited_per_dimension[i]) and (velo_this_dimension in velos_visited_per_dimension[i]):
            loop_intervals[i] = step_counter
        else:
            points_visited_per_dimension[i].append(coords_this_dimension)
            velos_visited_per_dimension[i].append(velo_this_dimension)

    if not step_counter % 10000:
        print(step_counter)
        print(loop_intervals)

print(loop_intervals)


