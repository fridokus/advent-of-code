lines = open('24.in').read().splitlines()

black = set()
tiles = []
for line in lines:
    tile = [0,0,0]
    i = iter(line)
    while i:
        try: c = next(i)
        except StopIteration: break
        if c == 'e':
            tile[0] += 1
            tile[1] -= 1
        elif c == 'w':
            tile[0] -= 1
            tile[1] += 1
        elif c == 's':
            c2 = next(i)
            if c2 == 'e':
                tile[0] += 1
                tile[2] -= 1
            else:
                tile[1] += 1
                tile[2] -= 1
        elif c == 'n':
            c2 = next(i)
            if c2 == 'e':
                tile[1] -= 1
                tile[2] += 1
            else:
                tile[0] -= 1
                tile[2] += 1
    tiles.append(tile)
    t = tuple(tile)
    if t in black: black.remove(t)
    else: black.add(t)

print(len(black))

def get_neighbors(tile):
    return [tuple([tile[i] + d[i] for i in range(3)]) for d in [(1,-1,0), (1,0,-1), (0,1,-1), (-1,1,0), (-1,0,1), (0,-1,1)]]

for _ in range(100):
    next_black = set()
    for tile in black:
        ns = get_neighbors(tile)
        count_black = 0
        for n in ns:
            if n in black: count_black += 1
        if 0 < count_black <= 2: next_black.add(tile)
        for n in ns:
            if n in black: continue
            n_of_ns = get_neighbors(n)
            count_black = 0
            for n_of_n in n_of_ns:
                if n_of_n in black: count_black += 1
            if count_black == 2: next_black.add(n)
    black = {i for i in next_black}

print(len(black))
