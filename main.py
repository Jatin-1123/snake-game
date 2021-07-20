from typing import Optional, List

import Strings


class Board:
    def __init__(self, size: int, board: Optional[List[List[int]]] = None) -> None:
        self.size: int = size
        self.board: List[List[int]] = board or [[0 for i in range(size)] for i in range(size)]

    def __str__(self) -> str:
        s = Strings.WALL_TOP_LEFT + (Strings.WALL_HORIZONTAL * self.size) + Strings.WALL_TOP_RIGHT + '\n'
        for row in self.board:
            s += Strings.WALL_VERTICAL
            for col in row:
                s += ' ' if not col else '*'
            s += Strings.WALL_VERTICAL + '\n'
        s += Strings.WALL_BOTTOM_LEFT + (Strings.WALL_HORIZONTAL * self.size) + Strings.WALL_BOTTOM_RIGHT
        return s


class Snake:
    def __init__(self, initial_size: int, board: Board) -> None:
        self.initial_size: int = initial_size
        self.board: Board = board
        self.input: str = "L"
        self.body: List[tuple[int, int]] = []
        self.body_set: set = set(self.body)

    def input(self, move_input):
        match move_input:
            case "L":
                pass
            case "R":
                pass
            case "D":
                pass
            case "U":
                pass


if __name__ == '__main__':
    board = Board(size=5)
    print(board)
