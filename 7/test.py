#Starting with my current IntCode impl, kept in a seperate file for reuse

class Instruction:
    def __init__(self, op_count, func):
        self.op_count = op_count
        self.func = func

class State:
    def __init__(self, memory, instruction_ptr):
        self.memory = memory
        self.instruction_ptr = instruction_ptr

class InputInterrupt(Exception):
    pass

class OutputInterrupt(Exception):
    pass

class IntCode:

    def mode_get(self, mode, operand):
        if mode:
            return operand
        else:
            return self.memory[operand]

    def add_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = a+b
        self.instruction_ptr += 4

    def multi_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = a*b
        self.instruction_ptr += 4

    def input_func(self, modes, operands):
        try:
            self.memory[operands[0]] = self.input_queue.popleft()
        except(IndexError):
            raise InputInterrupt
        else:
            # Only advance the instruction pointer if we haven't taken the 
            # input
            # hours_debugging: I don't want to talk about it
            self.instruction_ptr += 2


    def output_func(self, modes, operands):
        self.output_queue.append(self.mode_get(modes[0], operands[0]))
        self.instruction_ptr += 2
        raise OutputInterrupt

    def jmp_true_func(self, modes, operands):
        if(self.mode_get(modes[0], operands[0])):
            self.instruction_ptr = self.mode_get(modes[1], operands[1])
        else:
            self.instruction_ptr += 3
    
    def jmp_false_func(self, modes, operands):
        if(not self.mode_get(modes[0], operands[0])):
            self.instruction_ptr = self.mode_get(modes[1], operands[1])
        else:
            self.instruction_ptr += 3
            
    def lt_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = int(a<b)
        self.instruction_ptr += 4

    def eq_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = int(a==b)
        self.instruction_ptr += 4

    def __init__(self, prgm):
        self.instruction_list = {
            1: self.add_func,
            2: self.multi_func,
            3: self.input_func,
            4: self.output_func,
            5: self.jmp_true_func,
            6: self.jmp_false_func,
            7: self.lt_func,
            8: self.eq_func,
        }

        self.prgm_str = prgm
        self.memory = IntCode.parse(self.prgm_str)
        self.instruction_ptr = 0
        self.done = False
        self.input_queue = deque()
        self.output_queue = deque()
    
    @staticmethod
    def instruction_parse(num, inputs):
        opcode = [num % 100]
        num //= 100
        for _ in range(inputs):
            opcode.append(num % 10)
            num //= 10
        return tuple(opcode)

    def run(self):
        while(not self.done):
            curr = self.memory[self.instruction_ptr]
            if(curr % 100 == 99):
                self.done = True
                break
            instruction = self.instruction_list[(curr % 100)]
            opcode = IntCode.instruction_parse(curr, 4)
            instruction(
                opcode[1:], 
                self.memory[self.instruction_ptr+1:self.instruction_ptr+5]
            )

    @staticmethod
    def parse(prgm_str):
        prgm = list(
            map(
                int,
                prgm_str.split(',')
            )
        )

        return prgm

# Here's where the actual solution starts

# Part 1

# from intcode_v3 import IntCode, OutputInterrupt
from itertools import permutations
from collections import deque

def run_sequence(sequence, prgm):
    amp = 0
    for phase in sequence:
        computer = IntCode(open('in\\7.in').readline())
        computer.input_queue = deque([phase, amp])
        while(not computer.done):
            try:
                computer.run()
            except(OutputInterrupt):
                pass

        amp = computer.output_queue.popleft()

    return amp

# computer = IntCode(open('in\\7.in').readline())

sequences = permutations(range(5))
prgm = open('in\\7.in').readline()
max_sequence =max(sequences, key=lambda x: run_sequence(x, prgm))

print(max_sequence)
print(run_sequence(max_sequence, prgm))

# Part 2

# from intcode_v3 import IntCode, InputInterrupt, OutputInterrupt
# from itertools import permutations
# from collections import deque

def run_sequence(sequence, prgm):
    computers = list()
    for phase in sequence:
        computers.append(IntCode(prgm))
        computers[-1].input_queue.append(phase)

    i = -1
    computers[0].input_queue.append(0)
    while(True):
        i = (i+1) % 5
        while(not computers[i].done):
            try:
                computers[i].run()
            except(OutputInterrupt):
                computers[(i+1) % 5].input_queue.append(computers[i].output_queue[-1])
                continue
            except(InputInterrupt):
                break
        
        if(all(map(lambda x: x.done, computers))):
            break

    return computers[0].input_queue[-1]

prgm = open('in\\7.in').readline()

sequences = permutations(range(5,10))

max_sequence = max(sequences, key=lambda x: run_sequence(x, prgm))

print(max_sequence)
print(run_sequence(max_sequence, prgm))

