#!/usr/bin/python3
import re

with open('21.in') as f:
    data = f.read().replace('\n','')

l = re.findall(r'([\w+\s]+)\(contains ([\w+,?\s?]+)', data)
complete_ingredients_list = [(set(i.strip().split(' ')), {j.strip() for j in a.split(',')}) for i, a in l]

a_dict = dict()
all_i = set()
for ingredients, allergens in complete_ingredients_list:
    all_i |= ingredients
    for a in allergens:
        if a in a_dict: a_dict[a] &= ingredients
        else:           a_dict[a] = {i for i in ingredients}

cannot_contain_any_allergen = {i for i in all_i}
for k, v in a_dict.items():
    cannot_contain_any_allergen -= v

res1 = 0
for ingredients, allergens in complete_ingredients_list:
    for i in cannot_contain_any_allergen:
        if i in ingredients: res1 += 1

print(res1)

for k, v in a_dict.items():
    print(k)
    print(v)

# Solve part 2 through inspection (1 min)
