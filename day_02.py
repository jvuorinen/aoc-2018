from common import read_input
from collections import Counter


def solve_1(raw_in):
    counts = [Counter(l) for l in raw_in]
    occurs = lambda n, c: "".join(str(x) for x in c.values()).count(str(n)) > 0
    return sum([occurs(2, c) for c in counts]) * sum([occurs(3, c) for c in counts])


def solve_2(raw_in):
    words = [(w1, w2) for w1 in raw_in for w2 in raw_in if dissimilarity(w1, w2) == 1][0]
    return "".join(c1 for c1, c2 in zip(*words) if c1 == c2)


if __name__ == "__main__":
    raw_in = read_input("data/day_02.txt")

    answer_1 = solve_1(raw_in)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
