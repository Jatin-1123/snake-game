from typing import Optional

import Strings


class Board:
    def __init__(self, size: int, board: Optional[list] = None) -> None:
        self.size: int = size
        self.board: list = board or [[0 for i in range(size)] for i in range(size)]

    def __str__(self) -> str:
        s = Strings.WALL_TOP_LEFT + (Strings.WALL_HORIZONTAL * self.size) + Strings.WALL_TOP_RIGHT + '\n'
        for row in self.board:
            s += Strings.WALL_VERTICAL
            for col in row:
                s += ' ' if not col else '*'
            s += Strings.WALL_VERTICAL + '\n'
        s += Strings.WALL_BOTTOM_LEFT + (Strings.WALL_HORIZONTAL * self.size) + Strings.WALL_BOTTOM_RIGHT
        return s


if __name__ == '__main__':
    board = Board(size=5)
    print(board)
