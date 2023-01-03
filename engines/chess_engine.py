from os import system

from units.engine import Engine
from boards.chess_board import ChessBoard

__all__ = ['ChessEngine']


class ChessEngine(Engine):
    def draw(self, board: ChessBoard) -> None:
        output = '  ' + ' '.join([str(x) for x in range(board.get_size())]) + '\n'

        for i, row in enumerate(board.get_board()):
            output += f'{i} '
            for p in row:
                output += (p.get_color() if p is not None else ' ') + '|'

            output += '\n'  # + '--' * board.get_size() + '\n'

        system('cls')

        print(output)

    def input(self) -> dict:
        action = dict()
        return action

    def log(self, **kwargs):
        if kwargs.get('end') is None:
            kwargs['end'] = '\n'

        print(kwargs['text'], end=kwargs['end'])
