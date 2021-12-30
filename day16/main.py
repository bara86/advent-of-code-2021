from typing import NamedTuple
from functools import reduce


class Res(NamedTuple):
    value: str
    read: int
    version: int
    read_value: int


def decodeSubpackets(value: str) -> Res:

    inital_len = len(value)
    versions = int(value[:3], 2)
    packet_id = int(value[3:6], 2)
    length_type_id = value[6]
    value = value[7:]

    if length_type_id == "0":
        length_type_length = 15
    else:
        length_type_length = 11

    length = int(value[: length_type_length], 2)
    value = value[length_type_length:]
    read_values = []

    if length_type_id == "0":
        while length:
            res = decode(value)
            length -= res.read
            value = res.value
            versions += res.version
            read_values.append(res.read_value)
    elif length_type_id == "1":
        for _ in range(length):
            res = decode(value)
            value = res.value
            versions += res.version
            read_values.append(res.read_value)

    if packet_id == 0:
        res_value = sum(read_values)
    elif packet_id == 1:
        res_value = reduce(lambda v, vals: v * vals, read_values)
    elif packet_id == 2:
        res_value = min(read_values)
    elif packet_id == 3:
        res_value = max(read_values)
    elif packet_id == 5:
        res_value = int(read_values[0] > read_values[1])
    elif packet_id == 6:
        res_value = int(read_values[0] < read_values[1])
    else:
        res_value = int(read_values[0] == read_values[1])

    return Res(value, inital_len-len(value), versions, res_value)


def decodeOperator(value: str) -> Res:

    initial_len = len(value)
    version = int(value[:3], 2)
    value = value[6:]
    tot_value = ""
    while True:
        is_last_value = value[0] == "0"
        tot_value += value[1:5]
        value = value[5:]

        if is_last_value:
            break

    return Res(value, initial_len-len(value), version, int(tot_value, 2))


def decode(value: str) -> Res:

    packet_type = int(value[3: 6], 2)
    if packet_type == 4:
        return decodeOperator(value)
    else:
        return decodeSubpackets(value)


def main():
    with open('input.txt', 'r') as f:
        value = bin(int('1'+f.read(), 16))[3:]

    decoded = decode(value)

    print(f"Day 1, tot_versions {decoded.version} {decoded.read_value}")


if __name__ == "__main__":
    main()
