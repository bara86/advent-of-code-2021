from typing import List, Tuple

from collections import defaultdict


def part2(lines: List[List[int]], min_locations: List[Tuple[int, int]], debug_print=False) -> List[int]:
    already_visited = set()
    to_visit = set()

    area_for_min = defaultdict(set)

    for min_location in min_locations:
        i, j = min_location
        value = lines[i][j]

        already_visited = {(i, j)}
        area_for_min[(i, j)].add(((i, j), value))

        def addIfNeeded(i, j, value):
            if j != 0:
                if (i, j - 1) not in already_visited:
                    to_visit.add(((i, j - 1), value))
            if j < len(lines[i]) - 1:
                if (i, j + 1) not in already_visited:
                    to_visit.add(((i, j + 1), value))
            if i != 0:
                if (i - 1, j) not in already_visited:
                    to_visit.add(((i - 1, j), value))
            if i < len(lines) - 1:
                if (i + 1, j) not in already_visited:
                    to_visit.add(((i + 1, j), value))

        addIfNeeded(i, j, value)

        while to_visit:
            (next_i, next_j), original_value = to_visit.pop()
            next_value = lines[next_i][next_j]
            if next_value < 9:
                area_for_min[(i, j)].add(((next_i, next_j), next_value))
                addIfNeeded(next_i, next_j, next_value)
                already_visited.add((next_i, next_j))

    if debug_print:
        for i in range(len(lines)):
            line = []
            for j in range(len(lines[i])):
                trovato = None
                for k, v in area_for_min.items():
                    if trovato:
                        break
                    for idx, valore in enumerate(v):
                        if (i, j) == valore[0]:
                            trovato = valore[1]
                            break
                    if (i, j) == k:
                        trovato = lines[i][j]
                if trovato is not None:
                    line.append(str(trovato))
                else:
                    line.append('_' if lines[i][j] != 9 else '9')
            print(" ".join(line))

    return sorted([len(v) for v in area_for_min.values()], reverse=True)[:3]


def main():

    with open('input.txt', 'r') as f:
        lines = [[int(v) for v in line.strip()] for line in f.readlines()]

    tot = 0
    min_locations = []
    for i, line in enumerate(lines):
        for j, value in enumerate(line):
            left_is_higher = True if j == 0 else value < line[j-1]
            top_is_higher = True if i == 0 else value < lines[i-1][j]
            right_is_higher = True if j == len(line) - 1 else value < line[j+1]
            bottom_is_higer = True if i == len(lines) - 1 else value < lines[i+1][j]

            if left_is_higher and top_is_higher and right_is_higher and bottom_is_higer:
                tot += value + 1
                min_locations.append((i, j))

    print(f"Day 1 {tot}")

    tots = part2(lines, min_locations)
    print(f"Part 2: {tots}, {tots[0]*tots[1]*tots[2]}")


if __name__ == "__main__":
    main()
