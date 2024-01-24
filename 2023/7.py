 #!/usr/bin/python3

from itertools import product
from functools import cmp_to_key

with open('7.in') as f:
    lines0 = f.read().splitlines()

values = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        }

def typ(c):
    if c.count(c[0]) == 5: return 6
    if c.count(c[0]) == 4 or c.count(c[1]) == 4: return 5
    if any([c.count(c[i]) == 3 and c.count(c[j]) == 2 for i, j in product(range(4), range(4))]): return 4
    if any([c.count(c[i]) == 3 for i in range(3)]): return 3
    if any([c.count(c[i]) == 2 and c.count(c[j]) == 2 and c[i] != c[j] for i, j in product(range(4), range(4))]): return 2
    if any([c.count(c[i]) == 2 for i in range(4)]): return 1
    return 0

def first_better(c1, c2):
    c1, c2 = c1[0], c2[0]
    if typ(c1) > typ(c2): return 1
    elif typ(c1) < typ(c2): return -1
    for i in range(5):
        if c1[i] == c2[i]: continue
        return (values[c1[i]] > values[c2[i]]) * 2 - 1

lines = sorted([l.split() for l in lines0], key=cmp_to_key(first_better))
r1 = sum([(i+1) * int(lines[i][1]) for i in range(len(lines))]) 
print(r1)

values['J'] = 1
def typ(c):
    if any([c.count(c[i]) == 5 - c.count('J') for i in range(5)]) or c.count('J') == 5: return 6
    if any([c.count(c[i]) == 4 - c.count('J') for i in range(5)]): return 5
    if any([c.count(c[i]) == 3 - c.count('J') and c.count(c[j]) == 2 and c[i] != c[j] and c[j] != 'J' for i, j in product(range(5), range(5))]): return 4
    if any([c.count(c[i]) == 3 - c.count('J') for i in range(5)]): return 3
    if any([c.count(c[i]) == 2 and c.count(c[j]) == 2 and c[i] != c[j] for i, j in product(range(5), range(5))]): return 2
    if any([c.count(c[i]) == 2 - c.count('J') for i in range(5)]): return 1
    return 0

lines = sorted([l.split() for l in lines0], key=cmp_to_key(first_better))
r2 = sum([(i+1) * int(lines[i][1]) for i in range(len(lines))]) 
print(r2)
