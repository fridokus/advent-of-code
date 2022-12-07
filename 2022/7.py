#!/usr/bin/python3

with open('7.in') as f:
    output = f.read().splitlines()

def get_dir(f, d):
    if not d: return f
    return get_dir(f[d[0]], d[1:])

files = {'/': dict()}
pwd = []

for line in output:
    if line == '$ ls': continue
    wd = get_dir(files, pwd)
    if line[:3] == 'dir': wd[line[4:]] = dict()
    elif '..' in line:    pwd = pwd[:-1]
    elif '$ cd' in line:  pwd.append(line[5:])
    else:
        size, name = line.split()
        wd[name] = int(size)

sizes = []
def du(d):
    if type(d) == int: return d
    size = sum([du(d[k]) for k in d])
    sizes.append(size)
    return size

req = 30000000 - (70000000 - du(files))
r1 = 0
r2 = 70000000 
for size in sizes:
    if size < 100000: r1 += size
    if size > req: r2 = min(r2, size)

print(r1)
print(r2)
