#!/usr/bin/python3

with open('5.in') as f:
    lines = f.read().splitlines()

rows = []
columns = []
seat_ids = []
for line in lines:
    line = line.replace('F', '0')
    line = line.replace('L', '0')
    line = line.replace('B', '1')
    line = line.replace('R', '1')
    row = int(line[:7], 2)
    column = int(line[7:], 2)
    rows.append(row)
    columns.append(column)
    seat_ids.append(row * 8 + column)

print(max(seat_ids))
print(set(range(871)) - set(seat_ids))

