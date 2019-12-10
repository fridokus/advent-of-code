#!/usr/bin/python3

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


# f = open('test10.in', 'r')
f = open('10.in', 'r')
m_raw = f.readlines()
m = Map(m_raw)

m.calculate_all_seen_asteroids()
print(m.seen_map)
max_seen = max([max(row) for row in m.seen_map])
print(max_seen)

# b
