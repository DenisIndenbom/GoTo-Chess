from app import App

from games.wrong_checkers import Checkers
from engines.chess_engine import ChessEngine

app = App(Checkers(), ChessEngine())

app.run()
