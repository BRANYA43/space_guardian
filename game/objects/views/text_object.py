import pygame
from pygame import Surface

from game.config import *


class TextObject:
    def __init__(self, text: str, color: str | tuple[int, int, int] = TEXT_COLOR, font_name: str = FONT_NAME,
                 font_size: int = FONT_SIZE):
        self.text = text
        self.set_font(font_name, font_size)
        self.set_color(color)
        self._set_text_surface()
        self._set_text_rect()

    def draw(self, surface: Surface):
        surface.blit(self.text_surface, self.text_rect)

    def set_text(self, text: str):
        self.text = text
        self._set_text_surface()
        self._set_text_rect()

    def set_color(self, value: str | tuple[int, int, int]):
        self.color = value
        self._set_text_surface()
        self._set_text_rect()

    def set_font(self, name: str, size: int):
        self.font = pygame.font.SysFont(name, size)

    def _set_text_surface(self):
        self.text_surface = self.font.render(self.text, False, self.color)

    def _set_text_rect(self):
        self.text_rect = self.text_surface.get_rect()
