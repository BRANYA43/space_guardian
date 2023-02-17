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
        self.game_board = GameSurface(self._display.width,
                                      self._display.height - self._top_bar.height - self._bottom_bar.height)
        self._score = TextSurface('0')
        self._health = TextSurface('0')

        self.__set_up_params()

    def draw(self):
        self._display.surface.blit(self._top_bar.surface, self._top_bar.rect)
        self._display.surface.blit(self._bottom_bar.surface, self._bottom_bar.rect)
        self._display.surface.blit(self.game_board.surface, self.game_board.rect)

    def set_score(self, score: int):
        self._score.set_text(str(score))

    def set_health(self, health: int):
        self._health.set_text(str(health))

    def __set_up_params(self):
        self._top_bar.x = self._display.x
        self._top_bar.y = self._display.y
        self.game_board.x = self._display.x
        self.game_board.y = self._top_bar.height
        self._bottom_bar.x = self._display.x
        self._bottom_bar.x = self.game_board.height

        self._score.x = self._top_bar.x
        self._score.centery = self._top_bar.centery

        self._health.x = self._bottom_bar.x
        self._health.centery = self._bottom_bar.centery
