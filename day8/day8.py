from itertools import chain
from collections import Counter

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

list_of_bits = [set('cagedb'), set('ab'), set('gcdfa'), set('fbcad'), set('eafb'), set('cdfbe'), set('cdfgeb'),
                set('dab'), set('acedgfb'), set('cefabd')]


def main():
    with open('input.txt', 'r') as f:
        lines = list(line.strip() for line in f.readlines())

    results = [line.split('|')[1].strip().split(' ') for line in lines]

    c = Counter(map(len, chain(*results)))
    print("Part 1:", c[LEN_OF_1] + c[LEN_OF_4] + c[LEN_OF_7] + c[LEN_OF_8])

    tot = 0
    for result in results:
        value = ''.join(str(list_of_bits.index(set(v))) for v in result)
        print(value)


if __name__ == "__main__":
    main()
