import os

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
LOSS_SCORE = 0
WIN_SCORE = 6
DRAW_SCORE = 3

def get_file_path(filename):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, filename)


def get_shape_score(shape: str):
    if shape == "X" or shape == "A":
        return ROCK_SCORE
    if shape == "Y" or shape == "B":
        return PAPER_SCORE
    if shape == "Z" or shape == "C":
        return SCISSORS_SCORE
    
    print("something went wrong shape score")


def determine_outcome_score(shape: str, opponent_shape: str):
    if shape == "X":
        if opponent_shape == "A":
            return DRAW_SCORE
        if opponent_shape == "C":
            return WIN_SCORE
        else:
            return LOSS_SCORE

    if shape == "Y":
        if opponent_shape == "B":
            return DRAW_SCORE
        if opponent_shape == "A":
            return WIN_SCORE
        else:
            return LOSS_SCORE

    if shape == "Z":
        if opponent_shape == "C":
            return DRAW_SCORE
        if opponent_shape == "B":
            return WIN_SCORE
        else:
            return LOSS_SCORE
    
    print("something went wrong outcome score")

def get_score_line(line: str):
    score = get_shape_score(line[2])
    score += determine_outcome_score(line[2], line[0])
    return score


def get_score_file(filename):
    score = 0
    with open(get_file_path(filename)) as f:
        for line in f:
            score += get_score_line(line)
    
    return score


def get_score_part_2(opponent_shape, outcome):
    if outcome == "Y":
        return get_shape_score(opponent_shape) + DRAW_SCORE
    if outcome == "X" and opponent_shape == "A":
        return get_shape_score("C") + LOSS_SCORE
    if outcome == "X" and opponent_shape == "B":
        return get_shape_score("A") + LOSS_SCORE
    if outcome == "X" and opponent_shape == "C":
        return get_shape_score("B") + LOSS_SCORE
    if outcome == "Z" and opponent_shape == "A":
        return get_shape_score("B") + WIN_SCORE
    if outcome == "Z" and opponent_shape == "B":
        return get_shape_score("C") + WIN_SCORE
    if outcome == "Z" and opponent_shape == "C":
        return get_shape_score("A") + WIN_SCORE



def get_score_file_part_two(filename):
    score = 0
    with open(get_file_path(filename)) as f:
        for line in f:
            score += get_score_part_2(line[0], line[2])
    
    return score

filename = "input.txt"
score = get_score_file(filename)
print("part 1: " + str(score))

score = get_score_file_part_two(filename)
print("part 2: " + str(score))