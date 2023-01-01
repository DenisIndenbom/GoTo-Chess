from units.piece import Piece

__all__ = ['Checker']


class Checker(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)

    def validate_step(self, pos: tuple, target: tuple) -> bool:
        x, y = pos
        t_x, t_y = target

        return (x + 1 == t_x or x - 1 == t_x) and (y + 1 == t_y or y - 1 == t_y)
