from __future__ import annotations

import math
from typing import List

from enum import Enum


parenthesis = {'(': ')', '[': ']', '{': '}', '<': '>'}

error_parenthesis_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_parentesis_points = list(parenthesis)


class LineType(Enum):
    VALID = 0
    INCOMPLETE = 1
    INVALID = 2


def findInvalidChar(line: str) -> str:
    ps = ()

    for c in line:
        if c in parenthesis:
            ps += (c,)
            continue

        if not ps or c != parenthesis[ps[-1]]:
            return c
        ps = ps[:-1]

    return ""


def findIncompleteSeq(line: str) -> str:
    ps = ()

    for c in line:
        if c in parenthesis:
            ps += (c,)
            continue

        if not ps or c != parenthesis[ps[-1]]:
            return ""
        ps = ps[:-1]

    return ''.join(ps)


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    tot = sum((error_parenthesis_points[c] for c in (findInvalidChar(line) for line in lines) if c))
    print("Part 1", tot)

    incomplete_sequences = list(filter(None, (findIncompleteSeq(line) for line in lines)))
    print("incomplete", incomplete_sequences)

    somme = []
    for incomplete in incomplete_sequences:
        somma = 0
        for c in incomplete[::-1]:
            somma = somma * 5 + incomplete_parentesis_points.index(c)+1
        somme.append(somma)

    print("Part 2:", sorted(somme)[math.floor(len(somme)/2)])

if __name__ == "__main__":
    main()
