with open('2.in') as f:
    lines = [i.split() for i in f] 

x = sum([(i[0][0] == 'f') * int(i[1]) for i in lines]) 
y = sum([(i[0][0] == 'u') * int(i[1]) - (i[0][0] == 'd') * int(i[1]) for i in lines]) 

print(-x*y)

aim = x = y = 0 
for word, v in lines:
    v = int(v)
    if word[0] == 'd': aim += v
    elif word[0] == 'u': aim -= v
    else:   
        x += v  
        y -= aim * v 

print(-x*y)
