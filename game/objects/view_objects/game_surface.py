from pygame import Surface

from ..base_objects import BaseObject
from game.utils.decorators import check_value_type, validate_color_code
from game.utils.functions import validate_type


class GameSurface(BaseObject):
    def __init__(self, size: tuple[int, int], *, color: str = None, bg: Surface = None):
        super().__init__(Surface(size))
        self._color = validate_type(color, str | None)
        self._bg = validate_type(bg, Surface | None)
        self._blit_object_list = []

    def draw(self, surface: Surface):
        if self._color is not None:
            self.surface.fill(self._color)
        if self._bg is not None:
            self.surface.blit(self._bg, self._bg.get_rect())
        if self._blit_object_list:
            for object_ in self._blit_object_list:
                object_.draw(self.surface)
        super().draw(surface)

    @validate_color_code
    def set_color(self, value: str):
        self._color = value

    @check_value_type(Surface)
    def set_bg(self, image_: Surface):
        self._bg = image_

    def add_blit_object(self, obj):
        if 'draw' in obj.__dir__():
            self._blit_object_list.append(obj)
        else:
            raise ValueError('Object has to be method "draw()".')
