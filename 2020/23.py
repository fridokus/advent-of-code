#!/usr/bin/python3

cups = [int(i) for i in open('23.in').read()[:-1]]

current_index = 0
for _ in range(100):
    current = cups[current_index]
    to_move = []
    for i in range(current_index - 8, current_index - 5): to_move.append(cups.pop(min(i, 0)))
    destination = (current - 2) % 9 + 1
    while destination in to_move: destination = (destination - 2) % 9 + 1
    destination_index = (cups.index(destination) + 1) % 9
    for i in to_move[::-1]: cups.insert(destination_index, i)
    current_index = (cups.index(current) + 1) % 9

print(''.join(str(i) for i in cups[cups.index(1)+1:] + cups[:cups.index(1)]))

cups = [int(i) for i in open('23.in').read()[:-1]]

right_neighbor = dict()
for cup in cups: right_neighbor[cup] = cups[cups.index(cup) - 8]
right_neighbor[cups[8]] = 10
for i in range(10, 1000001): right_neighbor[i] = i + 1
right_neighbor[1000000] = current = cups[0]

for _ in range(10000000):
    to_move = [right_neighbor[current]]
    for _ in range(2): to_move.append(right_neighbor[to_move[-1]])
    right_neighbor[current] = right_neighbor[to_move[-1]]
    destination = (current - 2) % 1000000 + 1
    while destination in to_move: destination = (destination - 2) % 1000000 + 1
    right_neighbor[to_move[-1]] = right_neighbor[destination]
    right_neighbor[destination] = to_move[0]
    current = right_neighbor[current]

print(right_neighbor[1] * right_neighbor[right_neighbor[1]])
