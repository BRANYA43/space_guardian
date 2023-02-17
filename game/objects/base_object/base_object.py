from abc import ABC

from pygame import Surface, Rect

from game.utils.decorators import is_value_type
from game.utils.functions import get_valid_value


class BaseObject(ABC):
    def __init__(self, surface: Surface):
        self._surface = get_valid_value(Surface, surface)
        self._rect = self._surface.get_rect()

    @is_value_type(Surface)
    def draw(self, surface: Surface):
        surface.blit(self._surface, self._rect)

    @property
    def surface(self) -> Surface:
        return self._surface

    @surface.setter
    @is_value_type(int)
    def surface(self, value: Surface):
        self._surface = value

    @property
    def rect(self) -> Rect:
        return self._rect

    @rect.setter
    @is_value_type(Rect)
    def rect(self, value: Rect):
        self._rect = value

    @property
    def width(self) -> int:
        return self._rect.width

    @property
    def height(self) -> int:
        return self._rect.height

    @property
    def x(self) -> int:
        return self._rect.x

    @x.setter
    @is_value_type(int)
    def x(self, value: int):
        self._rect.x = value

    @property
    def y(self) -> int:
        return self._rect.y

    @y.setter
    @is_value_type(int)
    def y(self, value: int):
        self._rect.y = value

    @property
    def top(self) -> int:
        return self._rect.top

    @top.setter
    @is_value_type(int)
    def top(self, value: int):
        self._rect.top = value

    @property
    def bottom(self) -> int:
        return self._rect.bottom

    @bottom.setter
    @is_value_type(int)
    def bottom(self, value: int):
        self._rect.bottom = value

    @property
    def left(self) -> int:
        return self._rect.left

    @left.setter
    @is_value_type(int)
    def left(self, value: int):
        self._rect.left = value

    @property
    def right(self) -> int:
        return self._rect.right

    @right.setter
    @is_value_type(int)
    def right(self, value: int):
        self._rect.right = value

    @property
    def center(self) -> tuple[int, int]:
        return self._rect.center

    @center.setter
    @is_value_type(tuple)
    def center(self, value: tuple):
        self._rect.center = value

    @property
    def centerx(self) -> int:
        return self._rect.centerx

    @centerx.setter
    @is_value_type(int)
    def centerx(self, value: int):
        self._rect.centerx = value

    @property
    def centery(self) -> int:
        return self._rect.centery

    @centery.setter
    @is_value_type(int)
    def centery(self, value: int):
        self._rect.centery = value

    @property
    def topleft(self) -> int:
        return self._rect.topleft

    @topleft.setter
    @is_value_type(int)
    def topleft(self, value: int):
        self._rect.topleft = value

    @property
    def toprigth(self) -> int:
        return self._rect.topright

    @toprigth.setter
    @is_value_type(int)
    def toprigth(self, value: int):
        self._rect.topright = value

    @property
    def bottomleft(self) -> int:
        return self._rect.bottomleft

    @bottomleft.setter
    @is_value_type(int)
    def bottomleft(self, value: int):
        self._rect.bottomleft = value

    @property
    def bottomright(self) -> int:
        return self._rect.bottomright

    @bottomright.setter
    @is_value_type(int)
    def bottomright(self, value: int):
        self._rect.bottomright = value
