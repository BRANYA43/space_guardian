from pygame import Surface
from pygame.sprite import Group

from ..base_objects import BaseObject
from game.utils.decorators import check_value_type, validate_color_code
from game.utils.functions import validate_type


class GameSurface(BaseObject):
    def __init__(self, size: tuple[int, int], *, color: str = None, bg: Surface = None):
        super().__init__(Surface(size))
        self._color = validate_type(color, str | None)
        self._bg = validate_type(bg, Surface | None)
        self._blit_objects_ = []
        self._blit_groups_ = []

    def draw(self, surface: Surface):
        self._fill()
        self._blit_bg()
        self._blit_objects()
        self._blit_groups()
        super().draw(surface)

    def _fill(self):
        if self._color is not None:
            self.surface.fill(self._color)

    def _blit_bg(self):
        if self._bg is not None:
            self.surface.blit(self._bg, self._bg.get_rect())

    def _blit_objects(self):
        if self._blit_objects_:
            for obj in self._blit_objects_:
                obj.draw(self.surface)

    def _blit_groups(self):
        if self._blit_groups_:
            for group in self._blit_groups_:
                for obj in group:
                    obj.draw(self.surface)

    @validate_color_code
    def set_color(self, value: str):
        self._color = value

    @check_value_type(Surface)
    def set_bg(self, image_: Surface):
        self._bg = image_

    def add_blit_object(self, obj):
        if 'draw' in obj.__dir__():
            self._blit_objects_.append(obj)
        else:
            raise ValueError('Object has to be method "draw()".')

    @check_value_type(Group)
    def add_blit_group(self, group: Group):
        self._blit_groups_.append(group)

    @check_value_type(tuple)
    def add_blit_tuple(self, objs: tuple):
        for obj in objs:
            self.add_blit_object(obj)
