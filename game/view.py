import pygame

from config import *


class View:
    def __init__(self):
        from model import Model
        self._model: Model | None = None
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display_rect = self.display.get_rect()

    def set_model(self, model):
        self._model = model

    def draw(self):
        self.display.fill((0, 0, 0))
        self.player_draw()
        pygame.display.update()

    def player_draw(self):
        self._model.player.draw(self.display)
