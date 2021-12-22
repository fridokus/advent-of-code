#!/usr/bin/python3

from re import findall

with open('22.in') as f:
    lines = f.read().splitlines()

cubes_in = []
ons = []
for line in lines:
    ints = tuple(int(i) for i in findall(r'-?\d+', line))
    cubes_in.append([])
    ons.append(True if line[:2] == 'on' else False)
    for i in range(3):
        cubes_in[-1].append((ints[2*i], ints[2*i+1]))

cubes = []
for cube_in, on in zip(cubes_in, ons):
    #if any([limits[0] > 50 or limits[1] < -50 for limits in cube_in]): continue # add for A
    new_cubes = [cube_in] if on else []
    for cube in cubes:
        if any([cube_in[i][1] < cube[i][0] or cube_in[i][0] > cube[i][1] for i in range(3)]):
            new_cubes.append(cube)
            continue
        if cube_in[0][0] > cube[0][0]:
            new_cubes.append([(cube[0][0], cube_in[0][0] - 1), cube[1], cube[2]])
        if cube_in[0][1] < cube[0][1]:
            new_cubes.append([(cube_in[0][1] + 1, cube[0][1]), cube[1], cube[2]])
        if cube_in[1][0] > cube[1][0]:
            new_cubes.append([(max(cube_in[0][0], cube[0][0]), min(cube_in[0][1], cube[0][1])), (cube[1][0], cube_in[1][0] - 1), cube[2]])
        if cube_in[1][1] < cube[1][1]:
            new_cubes.append([(max(cube_in[0][0], cube[0][0]), min(cube_in[0][1], cube[0][1])), (cube_in[1][1] + 1, cube[1][1]), cube[2]])
        if cube_in[2][0] > cube[2][0]:
            new_cubes.append([(max(cube_in[0][0], cube[0][0]), min(cube_in[0][1], cube[0][1])),
                (max(cube_in[1][0], cube[1][0]), min(cube_in[1][1], cube[1][1])), (cube[2][0], cube_in[2][0] - 1)])
        if cube_in[2][1] < cube[2][1]:
            new_cubes.append([(max(cube_in[0][0], cube[0][0]), min(cube_in[0][1], cube[0][1])),
                (max(cube_in[1][0], cube[1][0]), min(cube_in[1][1], cube[1][1])), (cube_in[2][1] + 1, cube[2][1])])
    cubes = new_cubes

vol = 0
for cube in cubes:
    vol += (cube[0][1] - cube[0][0] + 1) * (cube[1][1] - cube[1][0] + 1) * (cube[2][1] - cube[2][0] + 1)

print(vol)
