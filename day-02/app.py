#!/usr/bin/env python3
#
################################################################################
#
#
#
################################################################################

input_file = 'day-02/input.txt'

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

opponent = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS
}

mine = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

def choose(theirs, mine):
    print('theirs:', theirs,'mine:', mine)
    # 0 if you lost,
    # 3 if the round was a draw,
    # 6 if you won
    if theirs == ROCK:
        if mine == ROCK:
            return 3
        if mine == PAPER:
            return 6
        if mine == SCISSORS:
            return 0
    if theirs == PAPER:
        if mine == ROCK:
            return 0
        if mine == PAPER:
            return 3
        if mine == SCISSORS:
            return 6
    if theirs == SCISSORS:
        if mine == ROCK:
            return 6
        if mine == PAPER:
            return 0
        if mine == SCISSORS:
            return 3
    return -1

def calc_selection_score (value):
    score = 0
    if value == ROCK:
        score = 1
    if value == PAPER:
        score = 2
    if value == SCISSORS:
        score = 3
    return score

# total_score = 0
# fh = open(input_file,"r")
# for line in fh.readlines():
#     play = line.split()
#     them = play[0]
#     me = play[1]
#
#     round_score = choose(opponent[play[0]], mine[play[1]])
#     selection_score = calc_selection_score(mine[play[1]])
#
#     total_score += round_score + selection_score
#
#     print('opponent:', play[0], 'me:', play[1], 'round score:', round_score, 'selection_score:', selection_score, 'total_score:', total_score)

################################################################################
# Part II
################################################################################

#
# X means you need to lose,
# Y means you need to end the round in a draw,
# Z means you need to win
#
def get_choice(theirs, outcome):
    print('theirs:', theirs,'outcome:', mine)
    # 0 if you lost,
    # 3 if the round was a draw,
    # 6 if you won
    if theirs == ROCK:
        if outcome == 'X':
            return SCISSORS
        if outcome == 'Y':
            return ROCK
        if outcome == 'Z':
            return PAPER
    if theirs == PAPER:
        if outcome == 'X':
            return ROCK
        if outcome == 'Y':
            return PAPER
        if outcome == 'Z':
            return SCISSORS
    if theirs == SCISSORS:
        if outcome == 'X':
            return PAPER
        if outcome == 'Y':
            return SCISSORS
        if outcome == 'Z':
            return ROCK

total_score = 0
fh = open(input_file,"r")
for line in fh.readlines():
    play = line.split()

    my_choice = get_choice(opponent[play[0]], play[1])
    round_score = choose(opponent[play[0]], my_choice)
    selection_score = calc_selection_score(my_choice)

    total_score += round_score + selection_score

    print('opponent:', play[0], 'outcome:', play[1], 'my_choice:', my_choice, )
    print('  round score:', round_score, 'selection_score:', selection_score, 'total_score:', total_score)

