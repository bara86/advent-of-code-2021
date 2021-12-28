from typing import Dict, Tuple

import heapq

def main():
    with open("input.txt", 'r') as f:
        lines = [[int(v) for v in line.strip()] for line in f.readlines()]

    distances = {}  # Dict[Tuple[int, int], int]
    parents = {}

    original_row, original_col = len(lines), len(lines[0])
    max_row, max_col = len(lines)*5, len(lines[0])*5
    destination = (max_row - 1, max_col - 1)

    def calculateValue(row, col):
        v = lines[row % original_row][col % original_col] + row // original_row + col // original_col
        if v > 9:
            return v - 9
        return v

    for row in range(max_row):
        for col in range(max_col):
            distances[(row, col)] = float('inf')
            parents[(row, col)] = None

    starting_point = (0, 0)
    distances[starting_point] = 0
    queue = [(0, starting_point)]
    visited = set()

    while queue:
        node = heapq.heappop(queue)[1]

        if node in visited:
            continue

        visited.add(node)

        if node == destination:
            break

        for row_inc, col_inc in (0, 1), (1, 0), (-1, 0), (0, -1):
            row = node[0] + row_inc
            col = node[1] + col_inc

            if row == max_row or col == max_col or row == -1 or col == -1:
                continue

            new_dist = calculateValue(row, col) + distances[node]
            if new_dist < distances[(row, col)]:
                distances[(row, col)] = new_dist
                parents[(row, col)] = node

                heapq.heappush(queue, (new_dist, (row, col)))

    nodes = tuple()
    current = destination
    while current in parents:
        nodes = (current,) + nodes
        current = parents[current]

    print([calculateValue(row, col) for row, col in nodes[1:]])

    print("Part 2:", sum(calculateValue(row, col) for row, col in nodes[1:]))


if __name__ == "__main__":
    main()
