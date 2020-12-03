#!/usr/bin/python3

with open('3.in') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
h = len(lines)
w = len(lines[0])
y = 0
x = 0

res1 = 0

while y < h - 1:
    y += 1
    x = (x + 3) % w
    res1 += lines[y][x] == '#'

print(res1)

# b

m_y_l = [1, 1, 1, 1, 2]
m_x_l = [1, 3, 5, 7, 1]
res2 = 1

for m_y, m_x in zip(m_y_l, m_x_l):
    y = 0
    x = 0
    crash = 0
    while y < h - 1:
        y += m_y
        x = (x + m_x) % w
        crash += lines[y][x] == '#'
    res2 *= crash

print(res2)
