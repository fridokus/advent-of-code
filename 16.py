#!/usr/bin/python3

import math
import numpy as np

base_pattern = [0, 1, 0, -1]

def calculate_element(n, i):
    bp_index = 0
    j = 0
    ret = 0
    for element in n:
        j += 1
        bp_index = (j // (i+1)) % 4
        ret += base_pattern[bp_index] * element

    return abs(ret) % 10

n_str = '030367993582'
index_message = int(n_str[:8])
n = list(map(int, n_str))
n_len = len(n)
phases = 100

# for phase in range(phases):
#     print('d')
#     new_n = []
#     for i in range(n_len):
#         element = calculate_element(n, i)
#         new_n.append(element)
#     n = [i for i in new_n]
# print(n[index_message:index_message+8])

mat = np.diag([1 for i in range(n_len)])
for row in range(1, n_len+1):
    mat[row-1] = np.concatenate([np.repeat(base_pattern, row) for i in range(math.ceil(n_len/row))])[1:n_len+1]

print(mat)
new_mat = mat
np.set_printoptions(suppress=True,linewidth=5000,threshold=5000)
for i in range(99):
    new_mat = mat.dot(new_mat)
    print(new_mat)
