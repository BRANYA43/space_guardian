import pygame
from pygame import Surface, Rect

from game.config import *
from game.utils import decorators, functions


class TextObject:
    def __init__(self, text: str, color: str | tuple[int, int, int] = TEXT_COLOR, font_name: str = FONT_NAME,
                 font_size: int = FONT_SIZE):
        self._text = functions.get_valid_value(str, text)
        self.set_font(font_name, font_size)
        self.set_color(color)
        self._set_text_surface()
        self._set_text_rect()

    @decorators.is_type_value(Surface)
    def draw(self, surface: Surface):
        surface.blit(self._text_surface, self._text_rect)

    @decorators.is_type_value(str)
    def set_text(self, text: str):
        self._text = text
        self._set_text_surface()
        self._set_text_rect()

    def set_color(self, value: str | tuple[int, int, int]):
        if type(value) in (str | tuple[int, int, int]):
            self._color = value
            self._set_text_surface()
            self._set_text_rect()
        else:
            raise TypeError('Color has to be code #000000 or rgb tuple (255, 255, 255).')

    def set_font(self, name: str, size: int):
        self._font = pygame.font.SysFont(name, size)

    def _set_text_surface(self):
        self._text_surface = self._font.render(self._text, False, self._color)

    def _set_text_rect(self):
        self._text_rect = self._text_surface.get_rect()

    @property
    def rect(self) -> Rect:
        return self._text_rect

    @property
    def top(self) -> int:
        return self._text_rect.top

    @top.setter
    @decorators.is_type_value(int)
    def top(self, value: int):
        self._text_rect.top = value

    @property
    def bottom(self) -> int:
        return self._text_rect.bottom

    @bottom.setter
    @decorators.is_type_value(int)
    def bottom(self, value: int):
        self._text_rect.bottom = value

    @property
    def left(self) -> int:
        return self._text_rect.left

    @left.setter
    @decorators.is_type_value(int)
    def left(self, value: int):
        self._text_rect.left = value

    @property
    def right(self) -> int:
        return self._text_rect.right

    @right.setter
    @decorators.is_type_value(int)
    def right(self, value: int):
        self._text_rect.right = value

    @property
    def center(self) -> tuple[int, int]:
        return self._text_rect.center

    @center.setter
    @decorators.is_type_value(tuple)
    def center(self, value: tuple):
        self._text_rect.center = value

    @property
    def centerx(self) -> int:
        return self._text_rect.centerx

    @centerx.setter
    @decorators.is_type_value(int)
    def centerx(self, value: int):
        self._text_rect.centerx = value

    @property
    def centery(self) -> int:
        return self._text_rect.centery

    @centery.setter
    @decorators.is_type_value(int)
    def centery(self, value: int):
        self._text_rect.centery = value

    @property
    def x(self) -> int:
        return self._text_rect.x

    @x.setter
    @decorators.is_type_value(int)
    def x(self, value: int):
        self._text_rect.x = value

    @property
    def y(self) -> int:
        return self._text_rect.y

    @y.setter
    @decorators.is_type_value(int)
    def y(self, value: int):
        self._text_rect.y = value

