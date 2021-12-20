from itertools import chain
from collections import Counter

from typing import List, Set, Tuple

LEN_OF_0 = 6
LEN_OF_1 = 2
LEN_OF_2 = 5
LEN_OF_3 = 5
LEN_OF_4 = 4
LEN_OF_5 = 5
LEN_OF_6 = 6
LEN_OF_7 = 3
LEN_OF_8 = 7
LEN_OF_9 = 6


def calculateDigit(result: List[str]) -> List[Set[str]]:

    def searchForLength(length):
        for i in result:
            if len(i) == length:
                return set(i)

    def searchFor1():
        return searchForLength(LEN_OF_1)

    def searchFor7():
        return searchForLength(LEN_OF_7)

    def searchFor4():
        return searchForLength(4)

    def searchFor8():
        return searchForLength(8)

    def searchFor0And9(digit_0_6: Set[str], digit_for_1: Set[str]) -> Tuple[Set[str], Set[str], Set[str]]:
        digit_for_0 = set()
        digit_for_6 = set()
        digit_for_9 = set()
        for i in result:
            if len(i) == LEN_OF_0:
                digits = set(i)
                if len(digit_0_6 - digits) == 1:
                    digit_for_0 = digits
                else:
                    if len(digit_for_1 - digits) == 0:
                        digit_for_9 = digits
                    else:
                        assert len(digit_for_1 - digits) == 1
                        digit_for_6 = digits

            if digit_for_0 and digit_for_9 and digit_for_6:
                break

        return digit_for_0, digit_for_6, digit_for_9

    def searchFor3(digit_for_1: Set[str]) -> Set[str]:
        for i in result:
            if len(i) == LEN_OF_3 and len(digit_for_1 - set(i)) == 0:
                return set(i)
        return set()

    def searchFor2and5(digit_5: str, digit_for_1: Set[str]) -> Tuple[Set[str], Set[str]]:
        digit_for_2 = set()
        digit_for_5 = set()
        for i in result:
            digits = set(i)
            if len(i) == LEN_OF_2 and len(digit_for_1 - digits) == 1:
                if digit_5 in digits:
                    digit_for_2 = digits
                else:
                    digit_for_5 = digits

        return digit_for_2, digit_for_5

    assert len(result) == 14

    digit_for_7 = searchFor7()
    digit_for_1 = searchFor1()
    digit_for_4 = searchFor4()
    digit_for_8 = set('abcdefg')

    upper_digit = digit_for_7 - digit_for_1
    digit_0_6 = digit_for_4 - digit_for_1

    digit_for_0, digit_for_6, digit_for_9 = searchFor0And9(digit_0_6, digit_for_1)
    digit_for_3 = searchFor3(digit_for_1)

    if digit_for_9:
        digit_5 = digit_for_8 - digit_for_9
    else:
        assert digit_for_3
        digit_5 = digit_for_8 - digit_for_4 - digit_for_3

    assert len(digit_5) == 1
    digit_for_2, digit_for_5 = searchFor2and5(next(iter(digit_5)), digit_for_1)

    assert upper_digit and digit_0_6

    return [digit_for_0, digit_for_1, digit_for_2, digit_for_3, digit_for_4, digit_for_5, digit_for_6,
            digit_for_7, digit_for_8, digit_for_9]


def main():
    with open('input.txt', 'r') as f:
        lines = list(line.strip() for line in f.readlines())

    results = [line.split('|')[1].strip().split(' ') for line in lines]

    c = Counter(map(len, chain(*results)))
    print("Part 1:", c[LEN_OF_1] + c[LEN_OF_4] + c[LEN_OF_7] + c[LEN_OF_8])

    total = 0
    for line in lines:
        digits = calculateDigit([v.strip() for v in line.replace(' | ', ' ').split(' ')])
        for i in range(len(digits)):
            assert digits[i] not in digits[i+1:], f"{i} {digits[i:].index(digits[i])}"

        results = line.split(' | ')[1].split(' ')
        value = ''.join(str(digits.index(set(result))) for result in results)
        total += int(value)

    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()
