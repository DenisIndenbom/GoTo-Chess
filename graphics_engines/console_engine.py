from os import system

from units.engine import Engine
from units.board import Board


class Console(Engine):
    def draw(self, board: Board) -> None:
        output = '  ' + ' '.join([str(x) for x in range(board.get_size())]) + '\n'

        for i, row in enumerate(board.get_board()):
            output += f'{i} '
            for p in row:
                output += (p.get_color() if p is not None else ' ') + '|'

            output += '\n'  # + '--' * board.get_size() + '\n'

        system('cls')

        print(output)

    def input_pos(self, **kwargs):
        piece_pos = tuple(map(int, input(kwargs['text']).split()))

        return piece_pos

    def log(self, **kwargs):
        print(kwargs['text'])
