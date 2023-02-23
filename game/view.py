import pygame
from pygame import Surface

from config import *
from objects import Display, GameSurface


class View:
    def __init__(self):
        from model import Model
        self._model: Model | None = None
        self.display = Display(DISPLAY_SIZE)
        self.top_bar = GameSurface(TOP_BAR_SIZE)
        self.game_board = GameSurface(GAME_BOARD_SIZE, color=BLACK)
        self.bottom_bar = GameSurface(BOTTOM_BAR_SIZE)
        self.score = ...
        self.timer = ...
        self.health = ...

    def set_up_params(self):
        self.top_bar.topleft = self.display.topleft
        self.game_board.top = self.top_bar.bottom
        self.bottom_bar.top = self.game_board.bottom

        self.game_board.add_blit_object(self._model.player)
        self.game_board.add_blit_object(self._model.player_projectiles)
        self.game_board.add_blit_object(self._model.alien_fleet)

    def set_model(self, model):
        self._model = model

    def draw(self):
        self.top_bar.draw(self.display.surface)
        self.bottom_bar.draw(self.display.surface)
        self.game_board.draw(self.display.surface)
        pygame.display.update()
