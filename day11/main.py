from typing import List, Tuple, Set


FLASH_THRESHOLD = 10


def flash(lines: List[List[int]], limits: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    flashes = []

    while limits:
        line_number, col = limits.pop(0)
        flashes.append((line_number, col))

        for i in range(line_number-1, line_number+2):
            for j in range(col-1, col+2):

                if (i, j) == (line_number, col):
                    continue

                if i < 0 or i == len(lines) or j < 0 or j == len(lines[line_number]):
                    continue

                lines[i][j] += 1
                if lines[i][j] == FLASH_THRESHOLD:
                    limits.append((i, j))
                    flashes.append((i, j))
                    lines[i][j] = 0

    return flashes


def increaseElement(lines: List[List[int]], row: int, col: int) -> Set[Tuple[int, int]]:

    tot = set()
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i, j) == (row, col):
                continue

            if i < 0 or i == len(lines) or j < 0 or j == len(lines[row]):
                continue

            if lines[i][j] == 0:
                continue

            lines[i][j] += 1
            if lines[i][j] == FLASH_THRESHOLD:
                tot.add((i, j))

    return tot


def increaseElements(lines: List[List[int]]) -> Set[Tuple[int, int]]:

    reached_limit = set()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            lines[row][col] += 1
            if lines[row][col] == FLASH_THRESHOLD:
                reached_limit.add((row, col))

    return reached_limit


def main():

    with open('input.txt', 'r') as f:
        lines = [[int(v) for v in line.strip()] for line in f.readlines()]

    sum = 0
    cycle = 0
    all_flash = False
    while not all_flash:
        cycle += 1
        reached_limit = increaseElements(lines)
        while reached_limit:
            row, col = reached_limit.pop()

            reached_limit |= increaseElement(lines, row, col)

        flashed = []
        all_flash = True
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] >= FLASH_THRESHOLD:
                    lines[i][j] = 0
                    flashed.append((i, j))
                else:
                    all_flash = False

        print(f"State {cycle}, {len(flashed)}, {flashed}")
        if cycle < 99:
            sum += len(flashed)

    print(f"Part 1 {sum}")
    print(f"Part 2 {cycle}")


if __name__ == "__main__":
    main()
