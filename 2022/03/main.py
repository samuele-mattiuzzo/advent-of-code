#!/usr/bin/python
from collections import Counter

INPUT = 'input.txt'
MODE = 'r'

LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ITEMS = LOWER+UPPER

def part_one_total(input_file):
    file_contents = input_file.read().split('\n')
    tot = 0
    for row in file_contents[:-1]:
        set_first = set(row[:int(len(row)/2)])
        set_second = set(row[int(len(row)/2):])
        commons = list(set_first.intersection(set_second))

        tot += sum([(ITEMS.index(common) + 1) for common in commons])
    return tot

def part_two_total(input_file):
    file_contents = input_file.read().split('\n')
    tot = 0
    for group in list(zip(*[iter(file_contents)]*3)):
        set_1 = "".join(list(set(group[0])))
        set_2 = "".join(list(set(group[1])))
        set_3 = "".join(list(set(group[2])))
        common = Counter(set_1 + set_2 + set_3).most_common()[0][0]
        tot += (ITEMS.index(common) + 1)
    return tot


if __name__ == "__main__":
    total = 0
    with open(INPUT, MODE) as input_file:
        # part 1
        # total = part_one_total(input_file)

        # part 2
        total = part_two_total(input_file)


    print(total)

    print(input_file.closed)
