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
        self.draw_player_projectiles()
        self.draw_player()
        self.draw_flot()
        pygame.display.update()

    def draw_player(self):
        self._model.player.draw(self.display)

    def draw_player_projectiles(self):
        for projectile in self._model.player_projectiles:
            projectile.draw(self.display)

    def draw_flot(self):
        for alien in self._model.flot:
            alien.draw(self.display)
