#!/usr/bin/python3

with open('17.in') as f:
    moves = [1 if i=='>' else 0 for i in f.read().strip()]

pieces = [
        [[1, 1, 1, 1]],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ],
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1],
        ],
        [
            [1],
            [1],
            [1],
            [1]
        ],
        [
            [1, 1],
            [1, 1]
        ]
    ]

w = 7
p = 0
m = 0
n_moves = len(moves)
top = 0
rocks = {(i, 0) for i in range(w)}
tops = []
rocks_sets = []
done = False
tops_per_first_iterations = []
final_stage = False
for iteration in range(2022 * 2022 * 2022):
    if done: break
    falling = set()
    for j in range(len(pieces[p])):
        for i in range(len(pieces[p][j])):
            if pieces[p][j][i]:
                falling |= {(2 + i, top + 4 + j)}
    while True == True:
        if moves[m]       and not any((f[0] == w-1 for f in falling)) \
                and not any({(f[0] + 1, f[1]) in rocks for f in falling}):
                    falling = {(f[0] + 1, f[1]) for f in falling}

        elif not moves[m] and not any((f[0] == 0   for f in falling)) \
                and not any({(f[0] - 1, f[1]) in rocks for f in falling}):
                    falling = {(f[0] - 1, f[1]) for f in falling}

        m = (m + 1) % n_moves
        if not {(f[0], f[1] - 1) for f in falling} & rocks:
            falling = {(f[0], f[1] - 1) for f in falling}
        else: break
    rocks |= falling
    top = max((r[1] for r in rocks))
    new_rocks = set()
    for r in rocks:
        if r[1] + 20 > top: new_rocks |= {r}
    rocks = new_rocks
    p = (p + 1) % 5
    if iteration == 2021: print(top)
    if iteration < 5 * n_moves:
        tops_per_first_iterations.append(top)
    if not iteration % (len(moves) * 5) and iteration and not final_stage:
        print('asdf')
        bot = min((r[1] for r in rocks))
        tops.append(top)
        rocks_sets.append({(r[0], r[1] - bot) for r in rocks})
        if len(rocks_sets) < 2: continue
        for i, s1 in enumerate(rocks_sets):
            for j, s2 in enumerate(rocks_sets):
                if s1 == s2 and i != j:
                    print(i, j)
                    final_stage = True
                    top_before_final = top
                    r2 = ((1000000000000 - (j+1) * (len(moves) * 5)) // ((len(moves) * 5) * (i - j))) * (tops[i] - tops[j])
                    r2 += tops[j]
                    anka = (1000000000000 - (j+1) * (len(moves) * 5)) % ((len(moves) * 5) * (i - j))
                    anka_counter = 0
                    break
    if final_stage:
        anka_counter += 1
        if anka_counter == anka:
            r2 += top - top_before_final
            done = True
print(tops)
print(r2)
# for y in range(22, 0, -1):
#     for x in range(w):
#         if (x, y) in rocks: print('#', end='')
#         elif (x, y) in falling: print('@', end='')
#         else: print('.', end='')
#     print()
