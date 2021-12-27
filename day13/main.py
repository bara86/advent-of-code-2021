from collections import defaultdict
from typing import Dict, Tuple


def foldAlongY(problem: Dict[Tuple[int, int], str], line: int, max_x: int, max_y: int) -> int:
    for y in range(line, max_y + 1):
        for x in range(max_x + 1):
            v = (x, line - (y - line))
            if problem[v] == '#':
                continue
            problem[v] = problem[(x, y)]

    return line - 1


def foldAlongX(problem: Dict[Tuple[int, int], str], line: int, max_x: int, max_y: int) -> int:
    for x in range(line, max_x + 1):
        for y in range(max_y + 1):
            v = (line - (x - line), y)
            if problem[v] == '#':
                continue
            problem[v] = problem[(x, y)]

    return line - 1


def main():
    max_x = max_y = 0
    with open('input.txt', 'r') as f:
        dots = []
        foldings = []
        initial_dots = True
        for line in f.readlines():
            line = line.strip()
            if not line:
                initial_dots = False
                continue
            if initial_dots:
                x, y = map(int, line.split(','))
                dots.append((x, y))
                max_x = max(x, max_x)
                max_y = max(y, max_y)
            else:
                foldings.append(line)

    problem = defaultdict(lambda: '.')
    for point in dots:
        problem[point] = '#'

    for folding in foldings:
        fold = folding.rsplit(' ', 1)[1]
        coordinate, line = fold.split('=')
        line = int(line)

        if coordinate == 'y':
            max_y = foldAlongY(problem, line, max_x, max_y)
        else:
            max_x = foldAlongX(problem, line, max_x, max_y)

    def printa():
        for y in range(max_y + 1):
            row = []
            for x in range(max_x + 1):
                row.append(problem[(x, y)])

            print(row)

    def countDots():
        dots = 0
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if problem[(x, y)] == '#':
                    dots += 1
        return dots

    # print(f"Part 1: dots {countDots()}")
    printa()

if __name__ == "__main__":
    main()
