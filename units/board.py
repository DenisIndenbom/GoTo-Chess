from units.piece import Piece

__all__ = ['Board']


class Board:
    def __init__(self, size) -> None:
        self.__board: list = [[None for _ in range(size)] for _ in range(size)]
        self.__size: int = size

    def get_board(self) -> list:
        return self.__board

    def get_size(self) -> int:
        return self.__size

    def set_piece(self, pos: tuple, piece: Piece) -> None:
        x, y = pos

        self.__board[y][x] = piece

    def get_piece(self, pos: tuple) -> Piece:
        return self.__board[pos[1]][pos[0]]

    def move(self, pos: tuple, target: tuple) -> bool:
        x, y = pos
        t_x, t_y = target

        if not ((0 <= x < self.__size) and (0 <= y < self.__size)) \
                or not ((0 <= t_x < self.__size) and (0 <= t_y < self.__size)) \
                or self.__board[y][x] is None:
            return False

        result = self.__board[y][x].validate_step(pos, target)

        if not result:
            return False

        self.__board[t_y][t_x] = self.__board[y][x]
        self.__board[y][x] = None

        return True
