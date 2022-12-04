import re
from typing import List, Tuple

from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD


def parse_input(d: str):
    data = []
    for x in d.split("\n"):
        match = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', x)
        a = int(match.group(1))
        b = int(match.group(2))
        c = int(match.group(3))
        d = int(match.group(4))
        m = max(a, b, c, d)
        data.append((
            bit_range(a, b, m),
            bit_range(c, d, m),
        ))
    return data


def bit_range(begin: int, end: int, m: int):
    binary = 0
    for i in range(0, m + 1):
        if i >= begin and i <= end:
            binary += 2 ** i
    return binary


def solve_a(d: List[Tuple[int, int]]):
    count = 0
    for a, b in d:
        both = a & b
        if a & both == a or b & both == b:
            count += 1
    return count


def solve_b(d: List[Tuple[int, int]]):
    count = 0
    for a, b in d:
        both = a & b
        if both > 0:
            count += 1
    return count


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=4)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
#     data = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""
    data = parse_input(data)

    # answer_a = solve_a(data)
    # print()
    # puzzle.answer_a = answer_a
    answer_b = solve_b(data)
    print()
    puzzle.answer_b = answer_b
