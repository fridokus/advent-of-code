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
    seat_id = int(line, 2)
    seat_ids.append(seat_id)

print(max(seat_ids))
print(set(range(871)) - set(seat_ids))

