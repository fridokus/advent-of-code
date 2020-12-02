#!/usr/bin/python3

from itertools import permutations
import time

class Computer(object):
    def __init__(self, instructions, inputs):
        self.inputs = inputs
        self.instructions = instructions
        self.pos = 0
        self.out = []
        self.stopped = False

    def halt(self):
        self.halted = True
        return self.out

    def advance_pos(self):
        self.pos += 1

    def execute(self):
        self.halted = False
        if self.stopped:
            return
        while not self.halted:
            op = int(str(self.instructions[self.pos])[-2:])
            modes = list(map(int, str(self.instructions[self.pos])[:-2])) # will miss leading zeros
            modes = [0 for i in range(10)] + modes # hack....
            self.advance_pos()
            self.apply_op(op, modes)

    def apply_op(self, op, modes):
        if op == 1:
            in_1 = self.read_value(modes.pop())
            in_2 = self.read_value(modes.pop())
            self.instructions[self.instructions[self.pos]] = in_1 + in_2
            self.advance_pos()

        elif op == 2:
            in_1 = self.read_value(modes.pop())
            in_2 = self.read_value(modes.pop())
            self.instructions[self.instructions[self.pos]] = in_1 * in_2
            self.advance_pos()

        elif op == 3:
            in_1 = self.inputs[0]
            self.inputs = self.inputs[1:]
            self.instructions[self.instructions[self.pos]] = in_1
            self.advance_pos()

        elif op == 4:
            self.out.append(self.instructions[self.instructions[self.pos]])
            self.advance_pos()
            self.halt()

        elif op == 5:
            if self.read_value(modes.pop()):
                self.pos = self.read_value(modes.pop())
            else:
                self.advance_pos()

        elif op == 6:
            if not self.read_value(modes.pop()):
                self.pos = self.read_value(modes.pop())
            else:
                self.advance_pos()

        elif op == 7:
            in_1 = self.read_value(modes.pop())
            in_2 = self.read_value(modes.pop())
            self.instructions[self.instructions[self.pos]] = int(in_1 < in_2)
            self.advance_pos()

        elif op == 8:
            in_1 = self.read_value(modes.pop())
            in_2 = self.read_value(modes.pop())
            self.instructions[self.instructions[self.pos]] = int(in_1 == in_2)
            self.advance_pos()

        elif op == 99:
            self.stopped = True
            self.halt()

        else:
            print('Unknown op ' + str(op))
            self.stopped = True
            self.halt()

    def read_value(self, mode):
        self.advance_pos()
        if mode:
            return self.instructions[self.pos-1]
        return self.instructions[self.instructions[self.pos-1]]


instructions = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]

instructions = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]


# instructions = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

max_output = 0
for phases in permutations(range(5)):
    input_ = 0
    for amp in range(5):
        computer = Computer(instructions, [phases[amp], input_])
        computer.execute()
        input_ = computer.out[-1]
    if input_ > max_output:
        max_output = input_

print(max_output)


# b

max_output = 0
for phases in permutations(range(5, 10)):
    computers = [Computer(instructions, [phases[i]]) for i in range(5)]
    amp = 0
    computers[-1].out = [0]
    while not all([i.stopped for i in computers]):
        computers[amp].inputs.append(computers[amp-1].out[-1])
        computers[amp].execute()
        amp = (amp + 1) % 5

    if computers[-1].out[-1] > max_output:
        max_output = computers[-1].out[-1]

print(max_output)

# ##
max_output = 0
loops = 5
for phases in permutations(range(5, 10)):
    input_ = 0
    computer_dict = {}
    for amp in range(5):
        computer_dict[amp] = Computer(instructions, [phases[amp], input_])
        print(computers[amp].inputs)
        computer_dict[amp].execute()
        input_ = computer_dict[amp].out[-1]
        print(computer_dict[amp].out)
        time.sleep(1)
        if computer_dict[amp].stopped:
            print('stop')

    for i in range(loops-1):
        for amp in range(5):
            # computer_dict[amp].pos = 0
            computer_dict[amp].inputs = [input_]
            print(computers[amp].inputs)
            computer_dict[amp].execute()
            input_ = computer_dict[amp].out[-1]
            print(computer_dict[amp].out)
            time.sleep(1)
            if computer_dict[amp].stopped:
                print('stop')

        if input_ > max_output:
            max_output = input_

print(max_output)

