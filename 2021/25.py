#!/usr/bin/python3

with open('25.in') as f:
    lines = [list(i) for i in f.read().splitlines()]

h = len(lines)
w = len(lines[0])

for step, moved in zip(range(200000), (False for i in range(200000))):
    new_lines = [['.' for i in range(w)] for j in range(h)]
    for j in range(h):
        for i in range(w):
            if lines[j][i] == '>':
                if lines[j][(i+1) % w] == '.': new_lines[j][(i+1) % w] = moved = '>'
                else: new_lines[j][i] = '>'
            elif lines[j][i] == 'v': new_lines[j][i] = 'v'
    lines = new_lines
    new_lines = [['.' for i in range(w)] for j in range(h)]
    for j in range(h):
        for i in range(w):
            if lines[j][i] == 'v':
                if lines[(j+1) % h][i] == '.': new_lines[(j+1) % h][i] = moved = 'v'
                else: new_lines[j][i] = 'v'
            elif lines[j][i] == '>': new_lines[j][i] = '>'
    lines = new_lines
    if not moved: break

print(step+1)
