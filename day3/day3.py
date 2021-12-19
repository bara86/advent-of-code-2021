from collections import Counter, defaultdict
from math import pow


def main():
    with open('input.txt', 'r') as f:
        lines = list(f.readlines())

    counters = [Counter() for _ in lines[0]]
    columns = [[] for _ in lines[0].strip()]
    possible_elements_oxigen = [line.strip() for line in lines]
    possible_elements_co2 = [line.strip() for line in lines]

    for i in range(len(lines[0].strip())):
        elements_oxigen = defaultdict(list)
        elements_co2 = defaultdict(list)

        for element in possible_elements_oxigen:
            elements_oxigen[element[i]].append(element)
        for element in possible_elements_co2:
            elements_co2[element[i]].append(element)

        if len(elements_oxigen['0']) > len(elements_oxigen['1']):
            possible_elements_oxigen = elements_oxigen['0'][:]
        else:
            possible_elements_oxigen = elements_oxigen['1'][:]

        if len(possible_elements_co2) > 1:
            if len(elements_co2['1']) < len(elements_co2['0']):
                possible_elements_co2 = elements_co2['1'][::]
            else:
                possible_elements_co2 = elements_co2['0'][:]
        # if len(possible_elements_oxigen) == 1:
        #     break

    print(possible_elements_oxigen, possible_elements_co2)

    def convert(value):
        tot = 0
        for i, v in enumerate(value[::-1]):
            tot += int(v) * pow(2, i)
        return tot

    print(convert(possible_elements_oxigen[0]) * convert(possible_elements_co2[0]))
    return
    for line in lines:
        for i, bit in enumerate(line.strip()):
            columns[i].append(bit)

    counters = [Counter(column) for column in columns]
    value = ''.join(counter.most_common(1)[0][0] for counter in counters)
    gamma = 0
    epsilon = 0
    for i, v in enumerate(value[::-1]):
        gamma += int(v) * pow(2, i)
        epsilon += (0 if v == '1' else 1) * pow(2, i)
    print(gamma, epsilon, gamma * epsilon)


if __name__ == "__main__":
    main()
