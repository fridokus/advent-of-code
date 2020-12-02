#!/usr/bin/python3

import intcode

prog = [1102,34915192,34915192,7,4,7,99,0]
prog = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

computer = intcode.IntCode(prog)

while not computer.done:
    computer.execute()

print(computer.out)

prog = intcode.parse_prog('in9.in')

inputs = [2]

computer = intcode.IntCode(prog, inputs)

while not computer.done:
    computer.execute()

print(computer.out)
