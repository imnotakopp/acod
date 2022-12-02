from typing import Any

from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD


def parse_input(d: str):
    """
    a little wrapper function to take the plain text and make it usable. This can be
    the hardest part sometimes ;)

    :param d:
    :return:
    """
    return d


def solve(d: Any):
    """

    :param d:
    :return:
    """
    return 42


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=1)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
    print(f'the input data is:')
    print(data)
    data = parse_input(data)

    answer_a = solve(data)

    print(f'little did they know, the answer is not {answer_a}')

    # submit your answer
    # TODO don't submit too many answers, you are limited / hour
    # puzzle.answer_a = answer_a
    # check the console
