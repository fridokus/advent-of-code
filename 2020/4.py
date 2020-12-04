#!/usr/bin/python3

with open('4.in') as f:
    lines = f.read().splitlines()

def check_valid(passport):
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False
    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            return False
    else:
        return False
    if not passport['hcl'][0] == '#':
        return False
    try:
        _ = int(passport['hcl'][1:], 16)
    except ValueError:
        return False
    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False
    if len(passport['pid']) != 9:
        return False
    return True

lines.append('')
passport_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
passports = [{}]

res1 = 0
res2 = 0
for line in lines:
    if not line:
        if all([i in passports[-1] for i in passport_keys]):
            res1 += 1
            res2 += check_valid(passports[-1])
        passports.append({})
        continue
    for item in line.split():
        k, v = item.split(':')
        passports[-1][k] = v

print(res1)
print(res2)
