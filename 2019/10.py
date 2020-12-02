#!/usr/bin/python3

import time

def gcd(x, y):
    if not x:
        return y
    if not y:
        return x
    gcd = 1
    if not x % y:
        return y

    for i in range(int(y / 2), 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    return gcd

class Map():
    def __init__(self, raw_map):
        self.raw_map = raw_map
        self.map = self.parse_map(self.raw_map)
        self.h = len(self.map)
        self.w = len(self.map[0])
        self.seen_map = [[0 for i in range(self.w)] for j in range(self.h)]

    def parse_map(self, m_in):
        m_out = []
        for line in m_in:
            m_out.append([])
            for char in line:
                if char == '.':
                    m_out[-1].append(0)
                elif char == '#':
                    m_out[-1].append(1)
        return m_out

    def calculate_all_seen_asteroids(self):
        for h in range(self.h):
            for w in range(self.w):
                if not self.map[h][w]:
                    continue
                self.calculate_seen_asteroids(h, w)

    def calculate_seen_asteroids(self, h, w):
        seen_asteroids = 0
        for i in range(self.h):
            for j in range(self.w):
                if not self.map[i][j] or (w == j and i == h):
                    continue
                dy = abs(i - h)
                dx = abs(j - w)
                divisor = gcd(dy, dx)
                step_y = (i - h) // divisor
                step_x = (j - w) // divisor
                y = h + step_y
                x = w + step_x
                seen_here = 1
                while x != j or y != i:
                    if self.map[y][x]:
                        seen_here = 0
                        break
                    y += step_y
                    x += step_x
                seen_asteroids += seen_here
        self.seen_map[h][w] = seen_asteroids

    def place_base(self):
        max_per_row = list(map(max, self.seen_map))
        indices_of_max_per_row = [self.seen_map[i].index(max_per_row[i]) for i in range(len(max_per_row))]
        index_of_max_y = max_per_row.index(max(max_per_row))
        index_of_max_x = indices_of_max_per_row[index_of_max_y]
        self.base = (index_of_max_y, index_of_max_x)
        self.map[self.base[0]][self.base[1]] = 2

    def calculate_angles(self):
        dydx_set = set()
        for i in range(self.h):
            for j in range(self.w):
                if j == self.base[1]:
                    continue
                dydx_set.add((i - self.base[0]) / (j - self.base[1]))
        self.target_list = []
        self.target_list.append((-100, 0)) # first target straight above 0
        dydx_list = sorted(list(dydx_set))
        print(dydx_list)
        for dydx in dydx_list:
            x = 0
            y = .1
            while (y % 1) != 0:
                x += 1
                y = x * dydx
            target = (int(100*y), 100*x)
            self.target_list.append(target)
        print(self.target_list)
        for i in self.map:
            print(i)
        print()
        print()
        self.target_list += [(-tup[0], -tup[1]) for tup in self.target_list]
        self.target_list = [(tup[0] + self.base[0], tup[1] + self.base[1]) for tup in self.target_list]

    def vaporize_all_asteroids(self):
        target_index = 0
        self.kill_count = 0
        while self.kill_count < 200:
            target = self.target_list[target_index]
            dy = abs(target[0] - self.base[0])
            dx = abs(target[1] - self.base[1])
            divisor = gcd(dx, dy)
            step_y = (target[0] - self.base[0]) // divisor
            step_x = (target[1] - self.base[1]) // divisor
            y = self.base[0] + step_y
            x = self.base[1] + step_x
            while (x != target[1] or y != target[0]) and self.w > x >= 0 and self.h > y >= 0:
                if self.map[y][x]:
                    # for i in self.map:
                    #     print(i)
                    # print()
                    # time.sleep(1)
                    self.map[y][x] = 0
                    self.kill_count += 1
                    if self.kill_count == 200:
                        print('200th kill: ' + str(y) + ',' + str(x))
                    break
                y += step_y
                x += step_x
            target_index += 1
            if target_index == len(self.target_list):
                target_index = 0


# f = open('test10.in', 'r')
f = open('10.in', 'r')
# f = open('test10_2.in', 'r')
# f = open('test10_3.in', 'r')
m_raw = f.readlines()
m = Map(m_raw)

m.calculate_all_seen_asteroids()
max_seen = max([max(row) for row in m.seen_map])
print(max_seen)
m.place_base()
m.calculate_angles()
m.vaporize_all_asteroids()

# b
