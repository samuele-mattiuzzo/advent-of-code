#!/usr/bin/python
from collections import Counter

INPUT = 'input.txt'
MODE = 'r'

def part_one_total(input_file):
    file_contents = input_file.read().split('\n')
    tot = 0
    for row in file_contents[:-1]:
        first_assignment, second_assignment = row.split(',')

        fa_start, fa_end = map(int, first_assignment.split('-'))
        sa_start, sa_end = map(int, second_assignment.split('-'))
        if (fa_start >= sa_start and fa_end <= sa_end) or \
           (sa_start >= fa_start and sa_end <= fa_end):
            tot += 1
    return tot

def part_two_total(input_file):
    file_contents = input_file.read().split('\n')
    tot = 0

    def assignment_to_range(assignment):
        to_list = list(map(int, assignment.split('-')))
        return range(int(to_list[0]), int(to_list[1])+1)

    for row in file_contents[:-1]:
        first_assignment, second_assignment = row.split(',')

        fa = assignment_to_range(first_assignment)
        sa = assignment_to_range(second_assignment)

        if (fa[0] in sa or fa[-1] in sa) or \
           (sa[0] in fa or sa[-1] in fa):
            tot += 1
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
