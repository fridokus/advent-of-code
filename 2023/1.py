#!/usr/bin/python3

import re

with open('1.in') as f:
    lines = f.read().splitlines()

word_to_digit = {
        'one': '1',
        'tw': '2',
        'three': '3',
        'four': '4',
        'fiv': '5',
        'six': '6',
        'seve': '7',
        'igh': '8',
        'nin': '9'
        }

r1 = r2 = 0
for line in lines:
    ints = re.findall(r'\d', line)
    r1 += int(''.join([ints[0], ints[-1]]))
    ints = re.findall(r'(\d|one|tw|three|four|fiv|six|seve|igh|nin)', line)
    ints = [i if i not in word_to_digit else word_to_digit[i] for i in ints]
    r2 += int(''.join([ints[0], ints[-1]]))
print(r1)
print(r2)
