#!/usr/bin/python3
# (7865555081.0, 1091) (3656293393.0, 2347) (5881645369.0, 1459) (3735881843.0, 2297)
# 2347 is a corner tile, 2053 is next to it (below rotated 180 deg)

tiles = {int(tile[5:9]): tile.split('\n')[1:] for tile in open('20.in').read().split('\n\n')}
image = [[] for i in range(12)]
# 0 = normal, 1 = 90 degrees, 2 = ... 4 = mirrored, 5 = mirrored 90 degrees, .. 7 = mirrored 270 degrees
image[0].append((2347, 0))

def flip(image): return [i[::-1] for i in image] 
def rotate(image): return list(zip(*image))[::-1]

def get_image(tile):
    if tile[1] == 0: return tiles[tile[0]]
    if tile[1] == 1: return rotate(tiles[tile[0]])
    if tile[1] == 2: return rotate(rotate(tiles[tile[0]]))
    if tile[1] == 3: return rotate(rotate(rotate(tiles[tile[0]])))
    if tile[1] == 4: return flip(tiles[tile[0]])
    if tile[1] == 5: return rotate(flip(tiles[tile[0]]))
    if tile[1] == 6: return rotate(rotate(flip(tiles[tile[0]])))
    if tile[1] == 7: return rotate(rotate(rotate(flip(tiles[tile[0]]))))

def get_all_orientations(tile_nr): return [get_image((tile_nr, i)) for i in range(8)]

def find_right_neighbor(tile):
    pattern = [i[-1] for i in get_image(tile)]
    print(pattern)

find_right_neighbor(image[0][-1])

# for i in range(12)):
#     # complete row
#     while len(image[i]) != 12:
#         image[i].append(find_right_neighbor(image[i][-1]))
    # add next row leftmost tile

