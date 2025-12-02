#! /usr/bin/env python3
with open('2.in', 'r') as f:
    full_input = f.read().split(',')

def get_invalid_ids(id_range: str) -> list[int]:
    start, end = map(int, id_range.split('-'))
    invalid_ids = set()
    for id_num in range(start, end + 1):
        id_str = str(id_num)
        length = len(id_str)
        if length % 2 == 0:
            half = length // 2
            if id_str[:half] == id_str[half:]:
                invalid_ids.add(id_num)
    return invalid_ids

all_invalid_ids = set()
for id_range in full_input:
    invalid_ids = get_invalid_ids(id_range)
    all_invalid_ids.update(invalid_ids)

print(sum(all_invalid_ids))

def get_invalid_ids(id_range: str) -> list[int]:
    start, end = map(int, id_range.split('-'))
    invalid_ids = set()
    for id_num in range(start, end + 1):
        id_str = str(id_num)
        length = len(id_str)
        for sub_len in range(1, length // 2 + 1):
            if length % sub_len == 0:
                times = length // sub_len
                if id_str[:sub_len] * times == id_str:
                    invalid_ids.add(id_num)
                    break
    return invalid_ids

all_invalid_ids = set()
for id_range in full_input:
    invalid_ids = get_invalid_ids(id_range)
    all_invalid_ids.update(invalid_ids)

print(sum(all_invalid_ids))
