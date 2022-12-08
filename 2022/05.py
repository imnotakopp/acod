import re
from typing import List, Tuple

from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD


def parse_input(d: str):
    crates, moves = d.split("\n\n")
    crates = [list(c) for c in crates.split("\n")]
    stacks = [i for i, v in enumerate(crates[-1]) if v != ' ']
    data = []
    for i in stacks:
        stack = []
        for c in crates:
            v = c[i]
            if v != ' ':
                stack.append(c[i])
        data.append(stack)
    return data, list(map(get_move, moves.split("\n")))


def get_move(m: str):
    match = re.match(r'move (\d+) from (\d+) to (\d+)', m)
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def solve_a(crates: List[List[str]], moves: Tuple[int, int, int]):
    for count, source, destination in moves:
        while count >= 1:
            crate = crates[source - 1][0]
            del crates[source - 1][0:1]
            crates[destination - 1].insert(0, crate)
            count -= 1
    return "".join([c[0] for c in crates])


def solve_b(crates: List[List[str]], moves: Tuple[int, int, int]):
    for count, source, destination in moves:
        crate = crates[source - 1][0:count]
        del crates[source - 1][0:count]
        crate.extend(crates[destination - 1])
        crates[destination - 1] = crate
        count -= 1
    return "".join([c[0] for c in crates])


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=5)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
#     data = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""
    crates, moves = parse_input(data)

    # answer_a = solve_a(crates, moves)
    # print()
    # puzzle.answer_a = answer_a
    answer_b = solve_b(crates, moves)
    # print()
    puzzle.answer_b = answer_b
