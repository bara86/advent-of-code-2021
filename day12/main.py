from collections import defaultdict, Counter
from typing import Dict, Set, Tuple


def checkIfPathIsValid(path: Tuple[str, ...]) -> bool:
    c = Counter([p for p in path if p.islower()])
    if c['start'] > 1:
        return False
    most_common = c.most_common(2)

    def calcRes():
        if not most_common:
            return True
        if most_common[0][1] == 1:
            return True
        if most_common[0][1] == 2 and len(most_common) == 1:
            return True
        if most_common[0][1] == 2 and most_common[1][1] == 1:
            return True

        return False
    return calcRes()


def main():
    connections = defaultdict(set)  # type: Dict[str, Set[str]]

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            start, end = line.strip().split('-')
            connections[start].add(end)
            if start != 'start':
                connections[end].add(start)

    connections = dict(connections)

    paths = {('start',)}
    tot_paths = set()
    while paths:
        new_paths = set()
        for path in paths:
            last_step = path[-1]

            for step in connections[last_step]:
                new_path = path + (step,)
                if step == 'end':
                    tot_paths.add(new_path)
                    continue

                if checkIfPathIsValid(new_path):
                    new_paths.add(new_path)
        paths = new_paths

    print(len(tot_paths))


if __name__ == "__main__":
    main()
