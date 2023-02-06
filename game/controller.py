import sys

import pygame
from pygame.event import Event

from game.global_vairables import LEFT, RIGHT
from model import Model


class Controller:
    def __init__(self, model: Model):
        self._model = model

    def handler_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.handler_keydonw_events(event)
            elif event.type == pygame.KEYUP:
                self.handler_keyup_events(event)

    def handler_keydonw_events(self, event: Event):
        if event.key == pygame.K_LEFT:
            self._model.player.set_moving_flag(LEFT, True)
        elif event.key == pygame.K_RIGHT:
            self._model.player.set_moving_flag(RIGHT, True)
        elif event.key == pygame.K_SPACE:
            self._model.player.attack()

    def handler_keyup_events(self, event: Event):
        if event.key == pygame.K_LEFT:
            self._model.player.set_moving_flag(LEFT, False)
        elif event.key == pygame.K_RIGHT:
            self._model.player.set_moving_flag(RIGHT, False)