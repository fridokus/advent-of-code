#!/usr/bin/python3

import pandas as pd
import numpy as np

def get_fuel(array):
    fuel = np.floor(array / 3) - 2
    if fuel < 0:
        return 0
    return fuel

data = pd.read_csv('input-1')

fuels_1 = np.floor(data['numbers'] / 3) - 2

print(sum(fuels_1))


fuel_total = 0
for module in data['numbers']:
    fuel = get_fuel(module)
    while fuel > 0:
        fuel_total += fuel
        fuel = get_fuel(fuel)

print(fuel_total)

    


