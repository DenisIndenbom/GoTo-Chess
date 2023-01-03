from abc import ABC, abstractmethod
from boards.chess_board import ChessBoard

__all__ = ['Engine']


class Engine(ABC):
    @abstractmethod
    def draw(self, board: ChessBoard) -> None:
        pass

    @abstractmethod
    def input(self) -> dict:
        action = dict()

        action['piece_pos'] = tuple(map(int, input().split()))
        action['target_pos'] = tuple(map(int, input().split()))

        return action

    @abstractmethod
    def log(self, **kwargs):
        pass
