#!/usr/bin/python3

import pandas as pd
import numpy as np

def apply_op(op, input_1, input_2):
    if op == 1:
        return input_2 + input_1
    
    if op == 2:
        return input_1 * input_2

    if op == 99:
        raise Exception

    raise Exception

def execute(program):
    pos = 0

    while True:
        op = program[pos]
        input_1 = program[program[pos + 1]]
        input_2 = program[program[pos + 2]]
        result_pos = program[pos + 3]

        try:
            result = apply_op(op, input_1, input_2)
            program[result_pos] = result
            pos += 4

        except Exception:
            return(program[0])


program_1 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]

program_1[1] = 12
program_1[2] = 2

print(execute(program_1))

# 2
for noun in range(100):
    for verb in range(100):
        program_2 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
        program_2[1] = noun
        program_2[2] = verb

        if execute(program_2) == 19690720:
            print(100*noun + verb)


