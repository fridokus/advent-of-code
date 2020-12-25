p = [int(i) for i in open('25.in').read().splitlines()]

def loop(n, s=7): return (n * s) % 20201227

l = [0, 0]
n = 1
i = 0
while not any(l):
    n = loop(n)
    i += 1
    if n == p[0]: l[0] = i
    elif n == p[1]: l[1] = i

n = 1
if l[0]:
    for _ in range(l[0]): n = loop(n, p[1])
elif l[1]:
    for _ in range(l[1]): n = loop(n, p[0])

print(n)
