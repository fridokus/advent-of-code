#!/usr/bin/python3

class InputError(Exception):
    pass

def popleft(l):
    ret = l[0]
    l = l[1:]
    return ret, l

class IntCode(object):
    def __init__(self, prog, inputs=None):
        self.prog = prog
        self.inputs = inputs
        self.done = False
        self.point = 0
        self.out = 0

    def execute(self):
        self.out_changed = False
        while not self.done and not self.out_changed:
            opcode_and_modes = [0 for i in range(5)] + list(map(int, str(self.prog[self.point]))) # handle missing zeros hack..
            modes = opcode_and_modes[:-2]
            opcode = int(''.join([str(i) for i in opcode_and_modes[-2:]]))
            self.point += 1
            self.run_opcode(modes, opcode)

    def read_value(self, modes):
        mode = modes.pop()
        if mode:
            ret = self.prog[self.point]
        else:
            ret = self.prog[self.prog[self.point]]
        self.point += 1
        return ret

    def run_opcode(self, modes, opcode):
        if opcode == 1:
            in_1 = self.read_value(modes)
            in_2 = self.read_value(modes)
            self.prog[self.prog[self.point]] = in_1 + in_2
            self.point += 1

        elif opcode == 2:
            in_1 = self.read_value(modes)
            in_2 = self.read_value(modes)
            self.prog[self.prog[self.point]] = in_1 * in_2
            self.point += 1

        elif opcode == 3:
            try:
                in_1, self.inputs = popleft(self.inputs)
            except IndexError:
                self.point -= 1
                raise InputError
            self.prog[self.prog[self.point]] = in_1
            self.point += 1

        elif opcode == 4:
            self.out = self.read_value(modes)
            self.out_changed = True

        elif opcode == 5:
            if self.read_value(modes):
                self.point = self.read_value(modes)
            else:
                self.point += 1

        elif opcode == 6:
            if not self.read_value(modes):
                self.point = self.read_value(modes)
            else:
                self.point += 1

        elif opcode == 7:
            in_1 = self.read_value(modes)
            in_2 = self.read_value(modes)
            if in_1 < in_2:
                self.prog[self.prog[self.point]] = 1
            else:
                self.prog[self.prog[self.point]] = 0
            self.point += 1

        elif opcode == 8:
            in_1 = self.read_value(modes)
            in_2 = self.read_value(modes)
            if in_1 == in_2:
                self.prog[self.prog[self.point]] = 1
            else:
                self.prog[self.prog[self.point]] = 0
            self.point += 1

        elif opcode == 99:
            self.point -= 1
            self.halt()

        else:
            print('Unknown opcode ' + str(opcode))
            self.halt()


    def halt(self):
        self.done = True
