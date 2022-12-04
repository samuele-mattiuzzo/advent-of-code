#!/usr/bin/python

INPUT = 'input.txt'
MODE = 'r'

LOSS = 0
DRAW = 3
WIN = 6

SHAPES = {    
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissor
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3   # scissor
}

WINS = ['CX', 'AY', 'BZ']
DRAWS = ['AX', 'BY', 'CZ']

player_score = 0

def round_scores(opp, pl):
    global player_score
    move = opp + pl
    if move in DRAWS:
        player_score += SHAPES[pl] + DRAW
    elif move in WINS: 
        player_score += SHAPES[pl] + WIN
    else:
        player_score += SHAPES[pl] + LOSS


if __name__ == "__main__":
    rounds = []
    with open(INPUT, MODE) as input_file:
        file_contents = input_file.read().split('\n')
        for round in file_contents:
            if round != '':
                opp, pl = round.split(' ')
                round_scores(opp, pl)

    # part 1
    print(player_score)

    print(input_file.closed)
