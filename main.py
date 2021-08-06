from typing import Optional

import Strings


class Board:
    def __init__(self, size: int, board: Optional[list[list[int]]] = None) -> None:
        self.size: int = size
        self.board: list[list[int]] = board or [[0 for i in range(size)] for i in range(size)]

    def __str__(self) -> str:
        s = Strings.WALL_TOP_LEFT + (Strings.WALL_HORIZONTAL * self.size) + Strings.WALL_TOP_RIGHT + '\n'
        for row in self.board:
            s += Strings.WALL_VERTICAL
            for col in row:
                s += ' ' if not col else '*'
            s += Strings.WALL_VERTICAL + '\n'
        s += Strings.WALL_BOTTOM_LEFT + (Strings.WALL_HORIZONTAL * self.size) + Strings.WALL_BOTTOM_RIGHT
        return s

    def neighbours(self, coord: tuple[int, int]) -> list[tuple[int, int]]:
        size = self.size - 1
        match coord:
            # CORNERS
            case (0, 0):
                return [(1, 0), (0, 1)]
            case (size, size):
                return [(size, size - 1), (size - 1, size)]
            case (0, size):
                return [(0, size - 1), (1, size)]
            case (size, 0):
                return [(size - 1, 0), (size, 1)]

            # EDGES
            case (0, x):
                return [(0, x - 1), (1, x), (0, x + 1)]
            case (size, x):
                return [(size, x - 1), (size - 1, x), (size, x + 1)]
            case (x, 0):
                return [(x - 1, 0), (x, 1), (x + 1, 0)]
            case (x, size):
                return [(x - 1, size), (x, size - 1), (x + 1, size)]

            # LITERALLY ANYTHING ELSE
            case (x, y):
                return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


class Snake:
    def __init__(self, initial_size: int, board: Board) -> None:
        self.initial_size: int = initial_size
        self.board: Board = board
        self.input: str = "L"
        self.body: list[tuple[int, int]] = []
        self.body_set: set = set(self.body)

    def input(self, move_input):
        self.input = move_input


if __name__ == '__main__':
    board = Board(size=5)
    print(board)
