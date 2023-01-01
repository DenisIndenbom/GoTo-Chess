from abc import ABC, abstractmethod
from units.board import Board

__all__ = ['Engine']


class Engine(ABC):
    @abstractmethod
    def draw(self, board: Board) -> None:
        pass

    @abstractmethod
    def input_pos(self, **kwargs):
        pass

    @abstractmethod
    def log(self, **kwargs):
        pass
