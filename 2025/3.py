#! /usr/bin/env python3
with open('3.in', 'r') as f:
    full_input = f.read().splitlines()


def find_highest_joltage(bank: str) -> int:
    highest_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > highest_joltage:
                highest_joltage = joltage
    return highest_joltage


print(sum(find_highest_joltage(bank) for bank in full_input))

def find_highest_joltage(bank: str, n: int=2) -> int:
    highest_joltage = ''
    while len(highest_joltage) < n:
        max_found, max_found_index = 0, 0
        for i in range(len(bank) - (n - len(highest_joltage)) + 1):
            if int(bank[i]) > max_found:
                max_found = int(bank[i])
                max_found_index = i
        highest_joltage += str(max_found)
        bank = bank[max_found_index + 1:]
    return int(highest_joltage)


print(sum(find_highest_joltage(bank, 12) for bank in full_input))
