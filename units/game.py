from abc import ABC, abstractmethod
from units.board import Board

__all__ = ['Game']


class Game(ABC):
    @abstractmethod
    def step(self, piece_pos: tuple, target_pos: tuple, second_player: bool) -> bool:
        return False

    @abstractmethod
    def init_board(self) -> None:
        pass

    @abstractmethod
    def check_win(self, second_player) -> bool:
        return False

    @abstractmethod
    def get_board(self) -> Board:
        return Board(0)
