from units.game import Game
from units.board import Board
from pieces.checker import Checker

__all__ = ['Checkers']


class Checkers(Game):
    def __init__(self):
        self.__board = Board(8)

    def init_board(self) -> None:
        for i in range(8):
            self.__board.set_piece((i, 0), Checker('b'))
            self.__board.set_piece((i, 1), Checker('b'))

        for i in range(8):
            self.__board.set_piece((i, 7), Checker('w'))
            self.__board.set_piece((i, 6), Checker('w'))

    def step(self, piece_pos, target_pos, second_player) -> bool:
        x, y = piece_pos
        t_x, t_y = target_pos

        if not ((0 <= x < 8) and (0 <= y < 8)) or not ((0 <= t_x < 8) and (0 <= t_y < 8)):
            return False

        if self.__board.get_piece(piece_pos) is None:
            return False

        if (self.__board.get_piece(piece_pos).get_color() == 'b' and not second_player) or \
                (self.__board.get_piece(piece_pos).get_color() == 'w' and second_player):
            return False

        if self.__board.get_piece(target_pos) is not None:
            if self.__board.get_piece(target_pos).get_color() == 'w' and not second_player or \
                    (self.__board.get_piece(piece_pos).get_color() == 'b' and second_player):
                return False

        return self.__board.move(piece_pos, target_pos)

    def check_win(self, second_player) -> bool:
        count = 0

        color = 'w' if second_player else 'b'

        for row in self.__board.get_board():
            for p in row:
                if p is None:
                    continue

                count += 1 if p.get_color() == color else 0

        return count == 0

    def get_board(self) -> Board:
        return self.__board
