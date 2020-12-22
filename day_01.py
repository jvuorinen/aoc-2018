from common import read_input
from itertools import cycle


def solve_1(raw_in):
    return eval("".join(raw_in))


def solve_2(raw_in):
    diffs = map(int, cycle(raw_in))
    s = 0
    visited = set([s])
    for d in diffs:
        s += d
        if s not in visited:
            visited.add(s)
        else:
            return s
        

if __name__ == "__main__":
    raw_in = read_input("data/day_01.txt")

    answer_1 = solve_1(raw_in)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
