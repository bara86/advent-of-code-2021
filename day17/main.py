from typing import Tuple


class Rect:

    def __init__(self, target: str):
        target_x, target_y = target.split(': ')[1].split(', ')

        def calculateLimit(v: str) -> Tuple[int, int]:
            values = [int(_v) for _v in v.split('=')[1].split('..')]

            return min(values), max(values)

        self.min_x, self.max_x = calculateLimit(target_x)
        self.min_y, self.max_y = calculateLimit(target_y)

    def test(self, point: Tuple[int, int]) -> bool:
        return self.min_x <= point[0] <= self.max_x and self.min_y <= point[1] <= self.max_y

    def over(self, point: Tuple[int, int]) -> bool:
        return point[0] > self.max_x or point[1] < self.min_y

    def __repr__(self):
        return f"Rect(\"Target area: x={self.min_x}..{self.max_x}, y={self.min_y}..{self.max_y}\")"


def main():
    with open('input.txt', 'r') as f:
        target_rect = Rect(f.readline())

    initial_pos = (0, 0)
    max_height = float('-inf')
    good_initial_speeds = set()

    for start_y in range(target_rect.min_y-1, -target_rect.min_y+1):
        for start_x in range(target_rect.max_x+1):
            point = initial_pos
            launch_max_height = float('-inf')
            velocity = [start_x, start_y]
            while True:

                if target_rect.over(point):
                    break

                if target_rect.test(point):
                    good_initial_speeds.add((start_x, start_y))
                    if launch_max_height > max_height:
                        max_height = launch_max_height

                launch_max_height = max(launch_max_height, point[1])
                point = point[0] + velocity[0], point[1] + velocity[1]

                if velocity[0] > 0:
                    velocity[0] -= 1
                if velocity[0] < 0:
                    velocity[0] += 1
                velocity[1] -= 1

    print(f"Part 1 {max_height}")
    print(f"Part 2 {len(good_initial_speeds)}")


if __name__ == "__main__":
    main()
