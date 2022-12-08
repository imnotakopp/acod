import re
from typing import List
from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()  # do not remove, this allows you to authenticate to AOCD


def parse_input(d: str):
    files = [
        {
            "path": "/",
            "type": "dir",
            "size": 0
        }
    ]
    pos = "/"
    for row in d.split("\n"):
        match = re.search(r'\$ cd (.+)', row, re.IGNORECASE)
        if match:
            value = match.group(1)
            if value == "..":
                pos = "/".join(pos.split("/")[0:-1])
            elif value == "/":
                pos = "/"
            else:
                pos += f"/{value}"
        elif row.startswith("$ ls"):
            continue
        elif row.startswith("dir"):
            directory = re.search(r'dir (.+)', row, re.IGNORECASE).group(1)
            files.append({"path": f"{pos}/{directory}", "type": "dir", "size": 0})
        else:
            match = re.search(r'(\d+) (.+)', row)
            size = match.group(1)
            name = match.group(2)
            files.append({"path": f"{pos}/{name}", "type": "file", "size": int(size)})
    return files


def solve_a(d: List[dict]):
    d.sort(key=lambda x : x.get("path"))
    for i in range(len(d) - 1, -1, -1):
        f = d[i]
        if f.get('type') == "dir":
            size = sum([_f.get("size") for _f in d if _f.get("path").startswith(f.get("path")) and _f.get("type") != "dir"])
            d[i]['size'] = size
    return sum([_f.get("size") for _f in d if _f.get("size") <= 100000 and _f.get('type') == "dir"])


def solve_b(d: List[dict]):
    d.sort(key=lambda x : x.get("path"))
    for i in range(len(d) - 1, -1, -1):
        f = d[i]
        if f.get('type') == "dir":
            size = sum([_f.get("size") for _f in d if _f.get("path").startswith(f.get("path")) and _f.get("type") != "dir"])
            d[i]['size'] = size
    root = [f.get("size") for f in d if f.get("path") == "/"][0]
    total = 70000000
    target = 30000000
    free = total - root
    return min([_f.get("size") for _f in d if _f.get("size") + free >= target and _f.get('type') == "dir"])


if __name__ == "__main__":
    # select the puzzle you are trying to solve
    puzzle = Puzzle(year=2022, day=7)

    # get input data, this is unique for every user and as plain text
    data = puzzle.input_data
#     data = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""
    data = parse_input(data)

    # answer_a = solve_a(data)
    # print()
    # puzzle.answer_a = answer_a
    answer_b = solve_b(data)
    # print()
    puzzle.answer_b = answer_b
