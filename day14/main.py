from collections import Counter, defaultdict
from itertools import tee
from typing import Iterator, List


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    starting_point = lines[0]
    v = (line.split(' -> ') for line in lines[2:])  # type: Iterator[List[str]]
    combinations = dict(v)

    first_value = starting_point[0]
    couples = Counter((''.join(v) for v in pairwise(starting_point)))
    tots = defaultdict(int)

    for i in range(40):
        tots = defaultdict(int)
        step = defaultdict(int)
        for couple, mul in couples.items():
            new_combination = f"{couple[0]}{combinations[couple]}", f'{combinations[couple]}{couple[1]}'
            step[new_combination[0]] += mul
            step[new_combination[1]] += mul
            tots[combinations[couple]] += mul
            tots[couple[1]] += mul
        couples = dict(step)
        tots[first_value] += 1

    most_common = Counter(tots).most_common()
    print("Tots: ", most_common[0][1] - most_common[-1][1])


if __name__ == "__main__":
    main()
