#!/usr/bin/python3
import re

data = open('21.in').read().replace('\n','')

l = re.findall(r'([\w+\s]+)\(contains ([\w+,?\s?]+)', data)
complete_ingredients_list = [(set(i.strip().split(' ')), {j.strip() for j in a.split(',')}) for i, a in l]

a_dict = dict()
all_i = set()
for ingredients, allergens in complete_ingredients_list:
    all_i |= ingredients
    for a in allergens:
        if a in a_dict: a_dict[a] &= ingredients
        else:           a_dict[a] = {i for i in ingredients}

cannot_contain_any_allergen = all_i - set.union(*[v for v in a_dict.values()])

print(sum(sum(i in ingredients for i in cannot_contain_any_allergen) for ingredients, _ in complete_ingredients_list))

while any(len(v) > 1 for _, v in a_dict.items()):
    for k in a_dict: 
        for k2, v in a_dict.items():
            if k != k2 and len(v) == 1: a_dict[k] -= v
res2 = ''
for _, v in sorted(a_dict.items(), key=lambda x: x[0]): res2 += next(iter(v)) + ','
print(res2[:-1])
