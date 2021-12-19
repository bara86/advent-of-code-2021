from typing import List, Dict, Tuple

from collections import defaultdict
from itertools import zip_longest


def isDiagoanl(start: Tuple[int, int], end: Tuple[int, int]) -> bool:
    return abs(start[0] - end[0]) == abs(start[1] - end[1])


def calculateRangeList(start: int, end: int) -> List[int]:
    return list(range(start, end + (1 if start <= end else -1), 1 if start <= end else -1))


def calculate(lines: List[str], want_diagonal: bool = False, debug: bool = False) -> Dict[Tuple[int, int], int]:
    d = defaultdict(int)

    for line in lines:
        s = line.strip().split(' -> ')
        if debug:
            print("line.split()", s)
        x_1, y_1 = map(int, s[0].split(','))
        x_2, y_2 = map(int, s[1].split(','))

        is_diagonal = want_diagonal and isDiagoanl((x_1, y_1), (x_2, y_2))
        if debug:
            print("is_diagonal", is_diagonal)
        if not (x_1 == x_2 or y_1 == y_2) and not is_diagonal:
            continue

        x_range = calculateRangeList(x_1, x_2)
        y_range = calculateRangeList(y_1, y_2)

        assert len(x_range) == len(y_range) or len(x_range) == 1 or len(y_range) == 1

        for x, y in zip_longest(x_range, y_range, fillvalue=x_range[0] if len(x_range) < len(y_range) else y_range[0]):
            if debug:
                print("x:", x, "y:", y)
            d[(x, y)] += 1

    return d


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    print("Part 1", sum(v > 1 for v in calculate(lines).values()))

    # 19812
    print("Part 2", sum(v > 1 for v in calculate(lines, want_diagonal=True).values()))


if __name__ == "__main__":
    main()
