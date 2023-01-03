from units.game import Game
from units.engine import Engine

__all__ = ['App']


class App:
    def __init__(self, game: Game, engine: Engine):
        self.game = game
        self.engine = engine
        self.input = input

        self.game.init()
        self.engine.draw(game.get_board())

        self.second_player = False

    def run(self):
        while True:
            action = self.engine.input()
            result = self.game.step(action, self.second_player)

            if not result:
                self.engine.log(text='Такой ход невозможен!')
                continue

            self.engine.draw(self.game.get_board())

            if self.game.check_win(self.second_player):
                self.engine.log(text=('Белый выиграл!' if not self.second_player else 'Чёрный выиграл!'))
                return

            self.second_player = not self.second_player
