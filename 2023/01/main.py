#!/usr/bin/python
import re

INPUT = 'input.txt'
MODE = 'r'


if __name__ == "__main__":
    sum = 0

    with open(INPUT, MODE) as input_file:
        file_contents = input_file.read().split('\n')
        for line in file_contents[:-1]:
            no_chars = re.sub('\D', '', line)
            sum += int(no_chars[0] + no_chars[-1])

    # part 1
    print(sum)
