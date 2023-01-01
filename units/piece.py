from abc import ABC, abstractmethod

__all__ = ['Piece']


class Piece(ABC):
    def __init__(self, color: str) -> None:
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    @abstractmethod
    def validate_step(self, pos: tuple, target: tuple) -> bool:
        return False
