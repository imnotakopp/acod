from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD


def parse_input(d: str):
    return d


def solve_a(d: str):
    i = 0
    while i + 4 < len(d):
        sub = d[i:i + 4]
        unique = len(set(list(sub)))
        if unique == len(sub):
            return i + 4
        i += 1
    return None


def solve_b(d: str):
    i = 0
    while i + 14 < len(d):
        sub = d[i:i + 14]
        unique = len(set(list(sub)))
        if unique == len(sub):
            return i + 14
        i += 1
    return None


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=6)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
    # data = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    # data = parse_input(data)

    # answer_a = solve_a(data)
    # puzzle.answer_a = answer_a
    answer_b = solve_b(data)
    # print()
    puzzle.answer_b = answer_b
