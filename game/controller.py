import sys

import pygame


class Controller:
    def __init__(self, model):
        self._model = model

    def handler_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
