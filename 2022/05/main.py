#!/usr/bin/python
from collections import Counter

INPUT = 'input.txt'
MODE = 'r'

# I went lazy here
stacks = {
    1: "QSWCZVFT",
    2: "QRB",
    3: "BZTQPMS",
    4: "DVFRQH",
    5: "JGLDBSTP",
    6: "WRTZ",
    7: "HQMNSFRJ",
    8: "RNFHW",
    9: "JZTQPRB"
}

def parse_instruction(instruction):
    num, start, target = [int(i) for i in instruction.split(' ') if i.isdigit()]
    return num, start, target

def get_mover_result(input_file, reverse=True):
    instructions = input_file.read().split('\n')
    reverse_idx = -1 if reverse else 1

    for instruction in instructions[:-1]:
        # read and parse the instruction line
        num, start, target = parse_instruction(instruction)
        # remove from start stack
        tmp = stacks[start][-num:]
        stacks[start] = stacks[start][:-num]
        # add in reverse (top to bottom) to the target stack
        stacks[target] = stacks[target] + tmp[::reverse_idx]
    
    tot = ''
    for itm in range(1,10):
        tot += stacks[itm][-1]

    return tot


if __name__ == "__main__":
    total = 0
    with open(INPUT, MODE) as input_file:
        # part 1
        # total = get_mover_result(input_file)

        # part 2
        total = get_mover_result(input_file, False)


    print(total)

    print(input_file.closed)
