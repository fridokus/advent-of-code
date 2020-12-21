#!/usr/bin/python3
# (7865555081.0, 1091) (3656293393.0, 2347) (5881645369.0, 1459) (3735881843.0, 2297)
# 2347 is a corner tile, 2053 is next to it (below rotated 180 deg)
SIZE = 12

tiles = {int(tile[5:9]): tile.splitlines()[1:] for tile in open('20.in').read().split('\n\n')}
image = [[] for i in range(SIZE)]
image[0].append((2297, 2))
# image[0].append((1951, 6))

def flip(image): return [list(i[::-1]) for i in image]
def rotate(image): return list(zip(*image))[::-1]

def get_image(tile):
    if tile[1] == 0: return flip(flip(tiles[tile[0]]))
    if tile[1] == 1: return rotate(tiles[tile[0]])
    if tile[1] == 2: return rotate(rotate(tiles[tile[0]]))
    if tile[1] == 3: return rotate(rotate(rotate(tiles[tile[0]])))
    if tile[1] == 4: return flip(tiles[tile[0]])
    if tile[1] == 5: return rotate(flip(tiles[tile[0]]))
    if tile[1] == 6: return rotate(rotate(flip(tiles[tile[0]])))
    if tile[1] == 7: return rotate(rotate(rotate(flip(tiles[tile[0]]))))

def get_all_orientations(k): return [get_image((k, o)) for o in range(8)]

def find_neighbor(tile, direction='right'):
    if direction == 'right': pattern = [i[-1] for i in get_image(tile)]
    else:                    pattern = get_image(tile)[-1]
    for k in tiles:
        if k == tile[0]: continue
        images = get_all_orientations(k)
        for o, image in enumerate(images):
            if  direction == 'right' and all(image[i][0] == pattern[i] for i in range(10)): break
            elif direction == 'down' and all(image[0][i] == pattern[i] for i in range(10)): break
        else: continue
        break
    return (k, o)

for i in range(SIZE):
    while len(image[i]) != SIZE: image[i].append(find_neighbor(image[i][-1]))
    if i != SIZE - 1: image[i+1].append(find_neighbor(image[i][0], direction='down'))

actual_image = [['.' for i in range(SIZE*8)] for j in range(SIZE*8)]
for j in range(SIZE):
    for i in range(SIZE):
        actual_part = [k[1:-1] for k in get_image(image[j][i])[1:-1]]
        for y in range(8):
            for x in range(8):
                actual_image[j*8 + y][i*8 + x] = actual_part[y][x]

monster = ['                  # ',
'#    ##    ##    ###',
' #  #  #  #  #  #   ']
monster_w = len(monster[0])
monster_h = len(monster)

def water_roughness(actual_image):
    hash_count = 0
    for row in actual_image:
        for i in row:
            if i == '#': hash_count += 1
    monsters_count = 0
    for j in range(8*SIZE - monster_h):
        for i in range(8*SIZE - monster_w):
            monster_here = True
            for y, row in enumerate(monster):
                for x, pixel in enumerate(row):
                    if pixel == '#' and actual_image[j+y][i+x] != '#':
                        monster_here = False
                        break
            monsters_count += monster_here

    return hash_count - 15*monsters_count

print(min([
    water_roughness(rotate(rotate(rotate(actual_image)))),
    water_roughness(rotate(rotate(actual_image))),
    water_roughness(rotate(actual_image)),
    water_roughness(actual_image),
    water_roughness(rotate(rotate(rotate(flip(actual_image))))),
    water_roughness(rotate(rotate(flip(actual_image)))),
    water_roughness(rotate(flip(actual_image))),
    water_roughness(flip(actual_image))
]))
