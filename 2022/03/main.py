#!/usr/bin/python

INPUT = 'input.txt'
MODE = 'r'

LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ITEMS = LOWER+UPPER

if __name__ == "__main__":
    total = 0
    with open(INPUT, MODE) as input_file:
        file_contents = input_file.read().split('\n')
        for row in file_contents[:-1]:
            set_first = set(row[:int(len(row)/2)])
            set_second = set(row[int(len(row)/2):])
            commons = list(set_first.intersection(set_second))

            total += sum([(ITEMS.index(common) + 1) for common in commons])

    print(total)

    print(input_file.closed)
