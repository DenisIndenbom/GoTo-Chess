from abc import ABC, abstractmethod
from units.piece import Piece

__all__ = ['Board']


class Board(ABC):
    def __init__(self, board, size: int) -> None:
        self._board = board
        self._size: int = size

    def get_board(self) -> list:
        return self._board

    def get_size(self) -> int:
        return self._size

    @abstractmethod
    def set_piece(self, pos: tuple, piece: Piece) -> None:
        pass

    @abstractmethod
    def get_piece(self, pos: tuple) -> Piece:
        pass

    @abstractmethod
    def move(self, pos: tuple, target: tuple) -> bool:
        pass
