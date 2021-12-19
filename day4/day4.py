from typing import List, Optional, Tuple


def foundWinner(extracted_numbers: List[str], b: List[List[List[str]]]) -> Optional[Tuple[List[List[str]], int]]:

    boards = {i: board for i, board in enumerate(b)}
    removed_boards = set()
    for number in extracted_numbers:
        for i, board in list(boards.items()):
            assert i not in removed_boards
            for line in board:
                if number in line:
                    line[line.index(number)] = '_'
                    if all(v == '_' for v in line):
                        del boards[i]
                    else:
                        for k in range(len(line)):
                            if all(l[k] == '_' for l in board):
                                del boards[i]

                    if not boards:
                        return board, int(number)
                    break


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        extracted_numbers = lines[0].split(',')
        boards = []
        board = []
        for line in lines[2:]:
            if not line:
                boards.append(board)
                board = []
                continue

            board.append(line.strip().split())
        else:
            boards.append(board)

    print(boards[0])

    res = foundWinner(extracted_numbers, boards)
    assert res is not None
    remains, number = res
    tot = 0
    for line in remains:
        assert all(v not in extracted_numbers[:extracted_numbers.index(str(number))] for v in line)
        tot += sum((int(v) if v != '_' else 0 for v in line))
    print(tot * number)


if __name__ == "__main__":
    main()
