import pygame

from config import *


class View:
    def __init__(self):
        self._model = None
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display_rect = self.display.get_rect()

    def set_model(self, model):
        self._model = model

    def draw(self):
        self.display.fill((255, 255, 0))
        pygame.display.update()
