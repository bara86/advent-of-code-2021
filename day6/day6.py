# coding=utf-8

from typing import Dict

from collections import Counter, defaultdict


def calculateLantern(initial_population: Dict[int, int], iterations: int) -> int:
    counter = dict(initial_population)

    for _ in range(iterations):
        new_lantern = defaultdict(int)

        for days_left, number in counter.items():
            days_left -= 1

            if days_left == -1:
                new_lantern[8] = number
                days_left = 6
            new_lantern[days_left] += number

        counter = new_lantern

    return sum(counter.values())


def main():
    with open('input.txt', 'r') as f:
        counter = Counter(map(int, f.readline().strip().split(',')))

    print("Day 1, tot:", calculateLantern(counter, 80))
    print("Day 2, tot:", calculateLantern(counter, 256))


if __name__ == "__main__":
    main()
