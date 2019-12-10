#!/usr/bin/python3

class Computer(object):
    def __init__(self, instructions, inputs):
        self.inputs = inputs[::-1]
        self.instructions = instructions
        self.pos = 0
        self.out = []

    def halt(self):
        print(self.out)
        raise Exception

    def advance_pos(self):
        self.pos += 1

    def execute(self):
        while True:
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
            in_1 = self.inputs.pop()
            self.instructions[self.instructions[self.pos]] = in_1
            self.advance_pos()

        elif op == 4:
            self.out.append(self.instructions[self.instructions[self.pos]])
            self.advance_pos()

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
            self.halt()

        else:
            print('Unknown op ' + str(op))
            self.halt()



    def read_value(self, mode):
        self.advance_pos()
        if mode:
            return self.instructions[self.pos-1]
        return self.instructions[self.instructions[self.pos-1]]


# a

inputs = [1]
instructions = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,34,224,101,-71,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1002,113,50,224,1001,224,-2550,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,13,50,225,102,7,187,224,1001,224,-224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,79,72,225,1101,42,42,225,1102,46,76,224,101,-3496,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,51,90,225,1101,11,91,225,1001,118,49,224,1001,224,-140,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,191,87,224,1001,224,-1218,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1,217,83,224,1001,224,-124,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,32,77,225,1101,29,80,225,101,93,58,224,1001,224,-143,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,45,69,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1108,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,509,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

# computer = Computer(instructions, inputs)
# computer.execute()


# b
# instructions = [3,9,7,9,10,9,4,9,99,-1,8] # pass
# instructions = [3,3,1108,-1,8,3,4,3,99] # pass
# instructions = [3,3,1107,-1,8,3,4,3,99] # pass
# instructions = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9] # pass
# instructions = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1] # pass
inputs = [5]
computer = Computer(instructions, inputs)
computer.execute()
