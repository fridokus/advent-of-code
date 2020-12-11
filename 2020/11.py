#!/usr/bin/python3

with open('11.in') as f:
    next_state = [list(i) for i in f.read().splitlines()]

h = len(next_state)
w = len(next_state[0])

def count_neighbors(state, j, i):
    neighbors = [state[y][x] == '#' if y >= 0 and y < h and x >= 0 and x < w and not (y == j and x == i) else False
            for y in range(j-1, j+2) for x in range(i-1, i+2)]
    return sum(neighbors)

state = 0
while state != next_state:
    state = [[i for i in row] for row in next_state]
    for j in range(h):
        for i in range(w):
            if state[j][i] == '.':
                next_state[j][i] = '.'
            elif state[j][i] == '#':
                next_state[j][i] = 'L' if count_neighbors(state, j, i) >= 4 else '#'
            else:
                next_state[j][i] = '#' if count_neighbors(state, j, i) == 0 else 'L'

print(sum([i == '#' for row in state for i in row]))
