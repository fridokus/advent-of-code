#!/usr/bin/python3

with open('7.in') as f:
    output = f.read().splitlines()

def get_dir(f, d):
    if not d: return f
    return get_dir(f[d[0]], d[1:])

def du(d):
    if type(d) == int: return d
    return sum([du(d[k]) for k in d])

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

req = 30000000 - (70000000 - du(files))
r1 = 0
r2 = 70000000 
def du_recursive(f):
    global r1, r2
    for k in filter(lambda x: type(f[x]) == dict, f):
        size = du(f[k])
        if size < 100000: r1 += size
        elif size > req:  r2 = min(r2, size)
        du_recursive(f[k])

du_recursive(files)
print(r1)
print(r2)
