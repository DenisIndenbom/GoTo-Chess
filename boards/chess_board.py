from units.board import Board
from units.piece import Piece

__all__ = ['ChessBoard']


class ChessBoard(Board):
    def __init__(self, size) -> None:
        super().__init__([[None for _ in range(size)] for _ in range(size)], size)

    def set_piece(self, pos: tuple, piece: Piece) -> None:
        x, y = pos

        self._board[y][x] = piece

    def get_piece(self, pos: tuple) -> Piece:
        return self._board[pos[1]][pos[0]]

    def move(self, pos: tuple, target: tuple) -> bool:
        x, y = pos
        t_x, t_y = target

        if not ((0 <= x < self._size) and (0 <= y < self._size)) \
                or not ((0 <= t_x < self._size) and (0 <= t_y < self._size)) \
                or self._board[y][x] is None:
            return False

        result = self._board[y][x].validate_step(pos, target)

        if not result:
            return False

        self._board[t_y][t_x] = self._board[y][x]
        self._board[y][x] = None

        return True
