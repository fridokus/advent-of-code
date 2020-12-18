#!/usr/bin/python3

with open('11.in') as f:
    lines = [list(i.strip()) for i in f]

h = len(lines)
w = len(lines[0])

def count_neighbors(state, j, i):
    neighbors = [state[y][x] == '#' if 0 <= y < h and 0 <= x < w and not (y == j and x == i) else False
            for y in range(j-1, j+2) for x in range(i-1, i+2)]
    return sum(neighbors)

def iterate_state(state, count_function, tol=4):
    next_state = 0
    while next_state != state:
        next_state = [[i for i in row] for row in state]
        for j in range(h):
            for i in range(w):
                if   next_state[j][i] == '.': state[j][i] = '.'
                elif next_state[j][i] == '#': state[j][i] = 'L' if count_function(next_state, j, i) >= tol else '#'
                else                        : state[j][i] = '#' if count_function(next_state, j, i) == 0   else 'L'
    return next_state

state = [[i for i in row] for row in lines]
next_state = iterate_state(state, count_neighbors)
print(sum([i == '#' for row in next_state for i in row]))

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
def count_neighbors_new(next_state, j, i):
    count = 0
    for direction in directions:
        distance = 0
        while True:
            distance += 1
            y, x = direction[0]*distance + j, direction[1]*distance + i
            if not (0 <= y < h and 0 <= x < w) or next_state[y][x] == 'L': break
            if next_state[y][x] == '#':
                count += 1
                break
    return count

state = [[i for i in row] for row in lines]
next_state = iterate_state(state, count_neighbors_new, tol=5)
print(sum([i == '#' for row in next_state for i in row]))
