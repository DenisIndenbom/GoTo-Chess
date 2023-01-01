from games.checkers import Checkers
from graphics_engines.console_engine import Console

game = Checkers()
game.init_board()
engine = Console()

second_player = False

engine.draw(game.get_board())

while True:
    piece_pos = engine.input_pos(text='Введите координаты шашки (x, y): ')
    target_pos = engine.input_pos(text='Введите координаты клетки (x, y): ')

    result = game.step(piece_pos, target_pos, second_player)

    if not result:
        engine.log(text='Такой ход невозможен!')
        continue

    engine.draw(game.get_board())

    if game.check_win(second_player):
        engine.log(text=('Белый выиграл!' if not second_player else 'Чёрный выиграл!'))
        input('Enter any key... ')
        exit(0)

    second_player = not second_player


