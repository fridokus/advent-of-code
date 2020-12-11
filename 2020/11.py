#!/usr/bin/python3

with open('11.in') as f:
    lines = [list(i) for i in f.read().splitlines()]

h = len(lines)
w = len(lines[0])

def count_neighbors(state, j, i):
    neighbors = [state[y][x] == '#' if y >= 0 and y < h and x >= 0 and x < w and not (y == j and x == i) else False
            for y in range(j-1, j+2) for x in range(i-1, i+2)]
    return sum(neighbors)

def iterate_state(next_state, count_function, tol=4):
    state = 0
    while state != next_state:
        state = [[i for i in row] for row in next_state]
        for j in range(h):
            for i in range(w):
                if state[j][i] == '.':
                    next_state[j][i] = '.'
                elif state[j][i] == '#':
                    next_state[j][i] = 'L' if count_function(state, j, i) >= tol else '#'
                else:
                    next_state[j][i] = '#' if count_function(state, j, i) == 0 else 'L'
    return state

next_state = [[i for i in row] for row in lines]
state = iterate_state(next_state, count_neighbors)
print(sum([i == '#' for row in state for i in row]))

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
def count_neighbors_new(state, j, i):
    count = 0
    for direction in directions:
        distance = 0
        while True:
            distance += 1
            y = direction[0]*distance + j
            x = direction[1]*distance + i
            if not (y >= 0 and y < h and x >= 0 and x < w): break
            if state[y][x] == '#':
                count += 1
                break
            if state[y][x] == 'L':
                break
    return count

next_state = [[i for i in row] for row in lines]
state = iterate_state(next_state, count_neighbors_new, tol=5)
print(sum([i == '#' for row in state for i in row]))
