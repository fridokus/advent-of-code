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

n_str = '03036732577212944063491565474664'
n_str = '59791875142707344554745984624833270124746225787022156176259864082972613206097260696475359886661459314067969858521185244807128606896674972341093111690401527976891268108040443281821862422244152800144859031661510297789792278726877676645835805097902853584093615895099152578276185267316851163313487136731134073054989870018294373731775466754420075119913101001966739563592696702233028356328979384389178001923889641041703308599918672055860556825287836987992883550004999016194930620165247185883506733712391462975446192414198344745434022955974228926237100271949068464343172968939069550036969073411905889066207300644632441054836725463178144030305115977951503567'
n = list(map(int, n_str))
index_message = int(''.join(map(str, n[:7])))
print(index_message)
n = n * 10000
n = n[index_message:]
n_len = len(n)
phases = 100

for phase in range(phases):
    sum_n = sum(n)
    new_n = []
    for i in range(n_len):
        element = abs(sum_n) % 10
        new_n.append(element)
        sum_n -= n[i]
    n = [i for i in new_n]
print(n[:8])

# mat = np.diag([1 for i in range(n_len)])
# for row in range(1, n_len+1):
#     mat[row-1] = np.concatenate([np.repeat(base_pattern, row) for i in range(math.ceil(n_len/row))])[1:n_len+1]

# print(mat)
# new_mat = mat
# np.set_printoptions(suppress=True,linewidth=5000,threshold=5000)
# for i in range(99):
#     new_mat = mat.dot(new_mat)
#     print(new_mat)
