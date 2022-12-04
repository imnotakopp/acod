from typing import List, Tuple

from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD


def parse_input(d: str):
    return [[l[0:int(len(l)/2)], l[int(len(l)/2):]] for l in d.split("\n")]


def solve_a(d: List[Tuple[str, str]]):
    # find a character in both
    c: str = None
    results = []
    for a, b in d:
        for _a in a:
            if _a in b:
                if _a == _a.lower():
                    results.append(ord(_a) - 96)
                else:
                    results.append(ord(_a) - 38)
                break
    return sum(results)


def solve_b(d: List[Tuple[str, str]]):
    """

    :param d:
    :return:
    """
    results = []
    for i in range(0, len(d), 3):
        a = "".join(d[i])
        b = "".join(d[i + 1])
        c = "".join(d[ i + 2])
        for _c in a:
            if _c in b and _c in c:
                if _c == _c.lower():
                    results.append(ord(_c) - 96)
                else:
                    results.append(ord(_c) - 38)
                break
    return sum(results)


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=3)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
#     data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""
    data = parse_input(data)

    # answer_a = solve_a(data)
    # puzzle.answer_a = answer_a
    answer_b = solve_b(data)
    # print()
    puzzle.answer_b = answer_b
