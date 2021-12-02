with open('2.in') as f:
    lines = [i.split() for i in f]

x = sum([(i[0][0] == 'f') * int(i[1]) for i in lines])
y = sum([(i[0][0] == 'u') * int(i[1]) - (i[0][0] == 'd') * int(i[1]) for i in lines])

print(-x*y)

aim = x = y = 0
for line in lines:
    if line[0][0] == 'd': aim += int(line[1])
    elif line[0][0] == 'u': aim -= int(line[1])
    else:
        x += int(line[1])
        y -= aim * int(line[1])

print(-x*y)
