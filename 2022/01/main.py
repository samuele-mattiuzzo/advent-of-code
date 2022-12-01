#!/usr/bin/python


INPUT = 'input.txt'
MODE = 'r'

def sum_calories(): pass

if __name__ == "__main__":
    all_totals = []
    highest = 0
    highest_top_3 = 0

    with open(INPUT, MODE) as input_file:
        file_contents = input_file.read().split('\n\n')
        for batch in file_contents[:-1]:
            batch_int = list(map(int, batch.split('\n')))
            all_totals.append(sum(batch_int))

    # part 1
    highest = sorted(all_totals, reverse=True)[0]
    print(highest)

    # part 2
    highest_top_3 = sum(sorted(all_totals, reverse=True)[0:3])
    print(highest_top_3)

    print(input_file.closed)
