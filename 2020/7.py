#!/usr/bin/python3
import re

with open('7.in') as f:
    lines = f.read().splitlines()

recipes = {}
for line in lines:
    product = re.match(r'\w+ \w+', line).group(0)
    counts = [int(i) for i in re.findall(r'\d', line)]
    components = [i[2:] for i in re.findall(r'\d \w+ \w+', line)]
    recipes[product] = [counts, components]

def parents(color):
    for product, ingredients in recipes.items():
        if any(color == component for component in ingredients[1]):
            for p in parents(product):
                yield p
            yield product

res1 = len(set(parents('shiny gold')))
print(res1)

def number_components(color):
    return 1 + sum(recipes[color][0][i] * number_components(recipes[color][1][i]) for i in range(len(recipes[color][0])))

res2 = number_components('shiny gold') - 1
print(res2)
