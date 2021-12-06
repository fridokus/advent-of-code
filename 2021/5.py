import re

with open('5.in') as f:
    lines = f.read().splitlines()

def calc_matrix(diag=False):
    m = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        x1, y1, x2, y2 = (int(i) for i in re.findall(r'\d+', line))
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2) + 1): m[x1][j] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1): m[i][y1] += 1
        elif diag:
            i = x1 
            j = y1
            while i != x2:
                m[i][j] += 1
                i += (x2 > x1) * 2 - 1
                j += (y2 > y1) * 2 - 1
            m[i][j] += 1

    r = 0
    for i in range(1000):
        for j in range(1000):
            if m[i][j] > 1: r += 1
    return r

print(calc_matrix(), calc_matrix(True))
