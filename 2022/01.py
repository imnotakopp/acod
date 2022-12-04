from typing import List

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
    return list(map(lambda x: None if x == '' else int(x), d.split("\n")))


def solve_b(d: List[int]):
    """

    :param d:
    :return:
    """
    gaps = [i for i in range(0, len(d)) if d[i] is None]
    elves = [sum(d[0:gaps[0]]), sum(d[gaps[-1] + 1:len(d)])]
    for i in range(0, len(gaps) - 1):
        begin = gaps[i] + 1
        end = gaps[i + 1]
        elves.append(sum(d[begin:end]))
    return sum(sorted(elves, reverse=True)[0:3])


def solve_a(d: List[int]):
    """

    :param d:
    :return:
    """
    gaps = [i for i in range(0, len(d)) if d[i] is None]
    elves = [sum(d[0:gaps[0]]), sum(d[gaps[-1] + 1:len(d)])]
    for i in range(0, len(gaps) - 1):
        begin = gaps[i] + 1
        end = gaps[i + 1]
        elves.append(sum(d[begin:end]))
    return max(elves)


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=1)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
    data = parse_input(data)

    # answer_a = solve_a(data)
    # puzzle.answer_a = answer_a
    answer_b = solve_b(data)
    puzzle.answer_b = answer_b
