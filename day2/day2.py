def main():
    with open('input.txt', 'r') as f:
        lines = list(map(lambda x: x.split(), f.readlines()))

    position = [0, 0, 0]
    for command, amount in lines:
        if command == "forward":
            position[1] += int(amount)
            position[0] += int(amount) * position[2]
        elif command == "down":
            # position[0] += int(amount)
            position[2] += int(amount)
        else:
            # position[0] -= int(amount)
            position[2] -= int(amount)
            # position[0] = max(position[0], 0)

    print(position[0] * position[1])


if __name__ == "__main__":
    main()
