from pygame import Surface

from ..base_object import BaseObject
from game.utils.decorators import is_value_type
from game.utils.functions import get_valid_value
from game.utils.custom_type import color_code


class GameSurface(BaseObject):
    def __init__(self, width: int, height: int, *, bg: Surface = None, color: str = None):
        super().__init__(Surface((width, height)))
        self._bg = get_valid_value(bg, Surface | None)
        self._color = get_valid_value(color, str | None)

    def draw(self, surface: Surface):
        if self._bg is not None:
            self._draw_bg()
        elif self._color is not None:
            self._fill_surface()
        super().draw(surface)

    def _draw_bg(self):
        self._surface.blit(self._bg, self._bg.get_rect())

    def _fill_surface(self):
        self._surface.fill(self._color)

    @is_value_type(Surface)
    def set_bg(self, image: Surface):
        self._bg = image

    @is_value_type(color_code)
    def set_color(self, value: color_code):
        self._color = value
