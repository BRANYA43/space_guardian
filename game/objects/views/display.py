import pygame

from game.objects.base_object import BaseObject


class Display(BaseObject):
    def __init__(self, size: tuple[int, int], title: str = ''):
        super().__init__(pygame.display.set_mode(size))
        pygame.display.set_caption(title)

    @property
    def display(self):
        return self.surface
