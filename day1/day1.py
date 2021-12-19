from typing import List


def countIncrease(values: List[int]) -> int:
    return len(list(filter(lambda x: x[0] < x[1], zip(values[:-1], values[1:]))))


def group(values: List[int]) -> List[int]:
    return [values[i] + values[i+1] + values[i+2] for i in range(len(values)-2)]


def main():
    with open('input.txt', 'r') as f:
        lines = list(map(int, f.readlines()))

    print(countIncrease(group(lines)))


if __name__ == "__main__":
    main()
