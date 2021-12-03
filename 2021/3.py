#!/usr/bin/python3

with open('3.in') as f:
    lines = f.read().splitlines()

l = len(lines[0])
sums = [sum([int(line[i]) for line in lines]) for i in range(l)]

gamma = ''.join([str(int(sums[i] >= len(lines)/2)) for i in range(l)])
epsilon = ''.join([str(int(not int(i))) for i in gamma])

print(int(gamma, 2) * int(epsilon, 2))

def shrink(lines, co):
    for i in range(l):
        most_one = sum([int(line[i]) for line in lines]) >= len(lines)/2
        lines = [line for line in lines if (most_one != co) != int(line[i])]
        if len(lines) == 1: return(lines[0])

print(int(shrink(lines, 0), 2) * int(shrink(lines, 1), 2))
