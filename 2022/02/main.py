#!/usr/bin/python

INPUT = 'input.txt'
MODE = 'r'

LOSS = 0
DRAW = 3
WIN = 6

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'
SHAPES_AND_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
    'X': LOSS,
    'Y': DRAW,
    'Z': WIN
}

player_score = 0

def round_scores(opp, result):
    global player_score
    opp_pt = SHAPES_AND_SCORES[opp]
    pl_pt = 0
    if result == 'Y':  # draw
        pl_pt = opp_pt
    elif result == 'Z':  # victory
        pl_pt = (opp_pt + 1) if opp_pt in [1, 2] else 1
    else:  # loss
        pl_pt = (opp_pt - 1) if opp_pt in [2, 3] else 3
    player_score += SHAPES_AND_SCORES[result]
    player_score += pl_pt


if __name__ == "__main__":
    rounds = []
    with open(INPUT, MODE) as input_file:
        file_contents = input_file.read().split('\n')
        for round in file_contents:
            if round != '':
                opp, result = round.split(' ')
                round_scores(opp, result)

    # part 1
    print(player_score)

    print(input_file.closed)
