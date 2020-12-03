#!/usr/bin/python3

with open('2.in') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]

res1 = 0
res2 = 0

for line in lines:
    dash_i = line.find('-')
    colon_i = line.find(':')
    mini = int(line[:dash_i])
    maxi = int(line[dash_i + 1:colon_i - 2])
    char = line[colon_i - 1]
    pwd = line[colon_i + 1:]
    res1 += mini <= pwd.count(char) <= maxi
    res2 += (line[colon_i + 1 + mini] == char) != (line[colon_i + 1 + maxi] == char)

print(res1)
print(res2)
