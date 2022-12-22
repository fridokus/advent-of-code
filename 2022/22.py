#!/usr/bin/python3

from re import findall

with open('22.in') as f:
    board, path = f.read().split('\n\n')

board = [list(i) for i in board.splitlines()]
w = len(board[0])
h = len(board)
for i in range(h):
    if len(board[i]) < w:
        board[i] += ' ' * (w - len(board[i]))

path = 'L' + path.strip() # to make them same length
distances = [int(i) for i in findall(r'\d+', path)]
turns = findall(r'[RL]', path)
assert len(turns) == len(distances)

def walk(p2):
    y, x = 0, 0
    for i in board[0]:
        if not i == ' ': break
        x += 1
    f = [1, 0] # face
    for t, d in zip(turns, distances):
        if t == 'L': f = [-f[1],  f[0]]
        else:        f = [ f[1], -f[0]]
        for _ in range(d):
            board[y][x] = {(0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'}[tuple(f)]
            y2, x2 = (y + f[0]) % h, (x + f[1]) % w
            if not p2:
                while board[y2][x2] == ' ':
                    y2, x2 = (y2 + f[0]) % h, (x2 + f[1]) % w
            f2 = f[:]
            if board[y2][x2] != ' ': pass
            elif p2 and f[0] == 1 and f[1] == 0:
                if x < 50:
                    y2, x2 = 0, 100 + x
                elif x < 100:
                    y2, x2 = x + 100, 49
                    f2 = [0, -1]
                else:
                    y2, x2 = x - 50, 99
                    f2 = [0, -1]
            elif p2 and f[0] == 0 and f[1] == 1:
                if y < 50:
                    y2, x2 = 149 - y, 99
                    f2 = [0, -1]
                elif y < 100:
                    y2, x2 = 49, y + 50
                    f2 = [-1, 0]
                elif y < 150:
                    y2, x2 = 149 - y, 149
                    f2 = [0, -1]
                else:
                    y2, x2 = 149, y - 100
                    f2 = [-1, 0]
            elif p2 and f[0] == -1 and f[1] == 0:
                if x < 50:
                    y2, x2 = 50 + x, 50
                    f2 = [0, 1]
                elif x < 100:
                    y2, x2 = 100 + x, 0
                    f2 = [0, 1]
                else:
                    y2, x2 = 199, x - 100
            elif p2 and f[0] == 0 and f[1] == -1:
                if y < 50:
                    y2, x2 = 149 - y, 0
                    f2 = [0, 1]
                elif y < 100:
                    y2, x2 = 100, y - 50
                    f2 = [1, 0]
                elif y < 150:
                    y2, x2 = 149 - y, 50
                    f2 = [0, 1]
                else:
                    y2, x2 = 0, y - 100
                    f2 = [1, 0]
            if board[y2][x2] == '#': break # don't update y, x, f
            y, x = y2, x2
            f = 1*f2
            board[y][x] = {(0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'}[tuple(f)] # for visualization
    return y, x, f

y, x, f = walk(False)
r1 = 1000*(y+1) + 4*(x+1) + {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}[tuple(f)]
print(r1)
y, x, f = walk(True)
r2 = 1000*(y+1) + 4*(x+1) + {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}[tuple(f)]
print(r2)
