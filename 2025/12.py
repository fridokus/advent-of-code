#!/usr/bin/env python3

data = open('test12.in').read().strip().split('\n\n')
shapes = [{(x, y) for y, line in enumerate(s.splitlines()[1:]) for x, char in enumerate(line) if char == '#'} for s in data[:-1]]

def can_place(shape, x_off, y_off, grid):
    for (x, y) in shape:
        if x + x_off >= w or y + y_off >= h or grid[x + x_off][y + y_off]:
            return False
    return True

def place(shape, x_off, y_off, val, grid):
    for (x, y) in shape:
        grid[x + x_off][y + y_off] = val

def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    return {(x - min_x, y - min_y) for x, y in shape}

def rotations(shape):
    current = shape
    for _ in range(4):
        yield current
        current = normalize({(y, -x) for x, y in current})

def flips(shape):
    yield shape
    yield normalize({(-x, y) for x, y in shape})

def variations(shape):
    for flipped_shape in flips(shape):
        for rotated_shape in rotations(flipped_shape):
            yield rotated_shape

def backtrack(i):
    if i == len(presents):
        return True

    original_shape = shapes[presents[i]]

    for shape in variations(original_shape):
        for x_off in range(w):
            for y_off in range(h):
                if can_place(shape, x_off, y_off, grid):
                    place(shape, x_off, y_off, 1, grid)
                    if backtrack(i + 1):
                        return True
                    place(shape, x_off, y_off, 0, grid)
    return False

r1 = 0
for line in data[-1].splitlines():
    grid_info, shape_str = line.split(': ')
    w, h = map(int, grid_info.split('x'))
    counts = list(map(int, shape_str.split(' ')))
    presents = []
    for shape_id, count in enumerate(counts):
        presents += [shape_id] * count

    grid = [[0 for _ in range(h)] for _ in range(w)]

    if backtrack(0):
        r1 += 1
        for g in grid:
            print(g)

print(r1)
