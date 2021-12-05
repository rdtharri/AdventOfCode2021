import numpy as np
from typing import List
import pyperclip


def iterate_horizontal(x_start: int, x_end: int, y: int) -> List[int]:
    current_x = x_start
    if x_start > x_end:
        while current_x >= x_end:
            yield [current_x, y]
            current_x += -1
    else:
        while current_x <= x_end:
            yield [current_x, y]
            current_x += 1


def iterate_vertical(y_start: int, y_end: int, x: int) -> List[int]:
    current_y = y_start
    if y_start > y_end:
        while current_y >= y_end:
            yield [x, current_y]
            current_y += -1
    else:
        while current_y <= y_end:
            yield [x, current_y]
            current_y += 1


def iterate_diagonal(start, end):

    current_x = start[0]
    current_y = start[1]
    if start[0] > end[0]:
        while current_x >= end[0]:
            if start[1] > end[1]:
                yield [current_x, current_y]
                current_x += -1
                current_y += -1
            else:
                yield [current_x, current_y]
                current_x += -1
                current_y += 1
    else:
        while current_x <= end[0]:
            if start[1] > end[1]:
                yield [current_x, current_y]
                current_x += 1
                current_y += -1
            else:
                yield [current_x, current_y]
                current_x += 1
                current_y += 1

    pass


def main():

    space = np.zeros((1000, 1000))
    x = 0
    y = 1

    with open("input.txt") as f:
        input_lines = [line.strip() for line in f.readlines()]

        paths = [
            [[int(el) for el in point.split(",")] for point in line.split(" -> ")]
            for line in input_lines
        ]

        for path in paths:

            if path[0][x] == path[1][x]:
                for point_x, point_y in iterate_vertical(
                    path[0][y], path[1][y], path[0][x]
                ):
                    space[point_y, point_x] = space[point_y, point_x] + 1
            elif path[0][y] == path[1][y]:
                for point_x, point_y in iterate_horizontal(
                    path[0][x], path[1][x], path[0][y]
                ):
                    space[point_y, point_x] = space[point_y, point_x] + 1

        print(f"Points over 1: {(space > 1).sum()}")
        pyperclip.copy(int((space > 1).sum()))

        space = np.zeros((1000, 1000))
        for path in paths:

            if path[0][x] == path[1][x]:
                for point_x, point_y in iterate_vertical(
                    path[0][y], path[1][y], path[0][x]
                ):
                    space[point_y, point_x] = space[point_y, point_x] + 1
            elif path[0][y] == path[1][y]:
                for point_x, point_y in iterate_horizontal(
                    path[0][x], path[1][x], path[0][y]
                ):
                    space[point_y, point_x] = space[point_y, point_x] + 1
            else:
                for point_x, point_y in iterate_diagonal(path[0], path[1]):
                    space[point_y, point_x] = space[point_y, point_x] + 1

        print(f"Points over 1: {(space > 1).sum()}")
        pyperclip.copy(int((space > 1).sum()))


if __name__ == "__main__":
    main()
