from abc import ABC, abstractmethod
from boards.chess_board import ChessBoard

__all__ = ['Game']


class Game(ABC):
    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def step(self, action: dict, second_player: bool) -> bool:
        return False

    @abstractmethod
    def check_win(self, second_player) -> bool:
        return False

    @abstractmethod
    def get_board(self) -> ChessBoard:
        return ChessBoard(0)
