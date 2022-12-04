from typing import List, Tuple

from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD

# ROCK, PAPER, SCISSORS
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
wins = {3: 2, 2: 1, 1: 3}
line = [3, 1, 2, 3, 1]
WIN = 6
DRAW = 3
LOSS = 0


def parse_input(d: str):
    """
    a little wrapper function to take the plain text and make it usable. This can be
    the hardest part sometimes ;)

    :param d:
    :return:
    """
    return [r.split(" ") for r in d.split("\n")]


def solve_a(d: List[Tuple[int, int]]):
    """

    :param d:
    :return:
    """
    scores = []
    for opp, me in d:
        opp_score = points[opp]
        my_score = points[me]
        outcome: int = None
        if wins[my_score] == opp_score:
            outcome = WIN
        elif opp_score == my_score:
            outcome = DRAW
        else:
            outcome = LOSS
        scores.append(my_score + outcome)
    return sum(scores)

def get_outcome(opp: int, my: int):
    if wins[my] == opp:
        return WIN
    elif opp == my:
        return DRAW
    else:
        return LOSS


def solve_b(d: List[Tuple[int, int]]):
    """

    :param d:
    :return:
    """
    scores = []
    my_outcomes = {'X': -1, 'Y': 0, 'Z': 1}
    for opp, me in d:
        opp_score = points[opp]
        my_play = line[opp_score + my_outcomes[me]]
        outcome = get_outcome(opp_score, my_play)
        scores.append(my_play + outcome)
    return sum(scores)




if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=2)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
#     data = """A Y
# B X
# C Z"""
    data = parse_input(data)

    # answer_a = solve_a(data)
    # puzzle.answer_a = answer_a
    answer_b = solve_b(data)
    # print()
    puzzle.answer_b = answer_b
