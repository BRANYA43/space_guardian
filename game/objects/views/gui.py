from pygame import Rect, Surface

from game.config import *
from .text_surface import TextSurface
from .game_surface import GameSurface
from .display import Display


class GUI:
    def __init__(self, display: Display):
        self._display = display
        self._top_bar = GameSurface(self._display.width, TILE * 2)
        self._bottom_bar = GameSurface(self._display.width, TILE * 2)
        self._game_board = GameSurface(self._display.width,
                                       self._display.height - self._top_bar.height - self._bottom_bar.height)
        self._score = TextSurface('SCORE 0')
        self._health = TextSurface('HEALTH 0')

        self.__set_up_params()

    def draw(self):
        self._top_bar.draw(self._display.surface)
        self._bottom_bar.draw(self._display.surface)
        self._game_board.draw(self._display.surface)
        self._score.draw(self._top_bar.surface)
        self._health.draw(self._bottom_bar.surface)

    def set_score(self, score: int):
        self._score.set_text(str(score))

    def set_health(self, health: int):
        self._health.set_text(str(health))

    def __set_up_params(self):
        self._score.x = self._top_bar.x + TILE
        self._score.centery = self._top_bar.centery

        self._health.x = self._bottom_bar.x + TILE
        self._health.centery = self._bottom_bar.centery

        self._top_bar.x = self._display.x
        self._top_bar.y = self._display.y
        self._game_board.x = self._display.x
        self._game_board.y = self._top_bar.height
        self._bottom_bar.x = self._display.x
        self._bottom_bar.y = self._game_board.height + self._top_bar.height


