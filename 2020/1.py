#!/usr/bin/python3

with open('1.in') as f:
    lines = f.readlines()
    lines = [int(i.strip()) for i in lines]
    l = len(lines)

for i in range(l):
    for j in range(l):
        if lines[i] + lines[j] == 2020:
            res1 = lines[i] * lines[j] 

print(res1)


# b


for i in range(l):
    for j in range(l):
        for k in range(l):
            if lines[i] + lines[j] + lines[k] == 2020:
                res2 = lines[i] * lines[j] * lines[k]

print(res2)
