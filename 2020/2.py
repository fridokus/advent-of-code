#!/usr/bin/python3

with open('2.in') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]

res1 = 0

for line in lines:
    dash_i = line.find('-')
    colon_i = line.find(':')
    mini = int(line[:dash_i])
    maxi = int(line[dash_i + 1:colon_i - 2])
    char = line[colon_i - 1]
    pwd = line[colon_i + 1:]
    res1 += pwd.count(char) <= maxi and pwd.count(char) >= mini

print(res1)
