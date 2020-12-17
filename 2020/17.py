#!/usr/bin/python3

with open('17.in') as f:
    start = f.read().replace('.', '0').replace('#', '1').splitlines()

size = 17
grid = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
for i, line in enumerate(start):
    for j, val in enumerate(line):
        grid[0][i][j] = int(val)

def iterate(grid):
    next_grid = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if grid[z][y][x] and 2 <= count_neighbors(grid, z, y, x) <= 3:
                    next_grid[z][y][x] = 1
                elif grid[z][y][x]:
                    next_grid[z][y][x] = 0
                elif count_neighbors(grid, z, y, x) == 3:
                    next_grid[z][y][x] = 1
                else:
                    next_grid[z][y][x] = 0
    return next_grid

def count_neighbors(grid, z, y, x):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if not (i == x and j == y and k == z) and grid[k%size][j%size][i%size]: count += 1
    return count

def count_total(grid):
    count = 0
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if grid[x][y][z]: count += 1
    return count

for i in range(6): grid = iterate(grid)
print(count_total(grid))

size = 18
grid = [[[[0 for i in range(size)] for j in range(size)] for k in range(size)] for l in range(size)]
for i, line in enumerate(start):
    for j, val in enumerate(line):
        grid[0][0][i][j] = int(val)

def iterate4d(grid):
    next_grid = [[[[0 for i in range(size)] for j in range(size)] for k in range(size)] for l in range(size)]
    for x in range(size):
        for y in range(size):
            for z in range(size):
                for w in range(size):
                    if grid[w][z][y][x] and 2 <= count_neighbors4d(grid, w, z, y, x) <= 3:
                        next_grid[w][z][y][x] = 1
                    elif grid[w][z][y][x]:
                        next_grid[w][z][y][x] = 0
                    elif count_neighbors4d(grid, w, z, y, x) == 3:
                        next_grid[w][z][y][x] = 1
                    else:
                        next_grid[w][z][y][x] = 0
    return next_grid

def count_neighbors4d(grid, w, z, y, x):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if not (i == x and j == y and k == z and l == w) and grid[l%size][k%size][j%size][i%size]: count += 1
    return count

def count_total4d(grid):
    count = 0
    for x in range(size):
        for y in range(size):
            for z in range(size):
                for w in range(size):
                    if grid[x][y][z][w]: count += 1
    return count

for i in range(6): grid = iterate4d(grid)
print(count_total4d(grid))
