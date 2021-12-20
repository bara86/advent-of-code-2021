from typing import List

from collections import namedtuple

FuelComsumptionFromPosition = namedtuple('FuelConsumptionFromPosition', ('consumption', 'position'))


def calculateDistance(position: int, target: int, exponential: bool = False) -> int:
    difference = abs(position - target)
    if not exponential:
        return difference

    return (difference + 1) * difference // 2


def calculateBest(positions: List[int], exponential: bool = False) -> FuelComsumptionFromPosition:
    max_position = max(positions)

    best_position = FuelComsumptionFromPosition(float('inf'), -1)
    for i in range(max_position + 1):
        consumption = sum(map(lambda x: calculateDistance(x, i, exponential), positions))

        if consumption < best_position.consumption:
            best_position = FuelComsumptionFromPosition(consumption, i)

    return best_position


def main():
    with open('input.txt', 'r') as f:
        positions = list(map(int, f.readline().strip().split(',')))

    best_position_day1 = calculateBest(positions)
    print(f"Day 1: Position {best_position_day1.position}, consumption {best_position_day1.consumption}")

    best_position_day2 = calculateBest(positions, exponential=True)
    print(f"Day 2: Position {best_position_day2.position}, consumption {best_position_day2.consumption}")


if __name__ == "__main__":
    main()
