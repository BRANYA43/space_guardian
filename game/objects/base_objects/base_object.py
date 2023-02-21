from abc import ABC

from pygame import Surface, Rect

from game.utils.decorators import is_value_type


class BaseObject(ABC):
    def __init__(self, surface: Surface):
        self._surface = surface
        self._rect = self._surface.get_rect()

    def draw(self, surface: Surface):
        surface.blit(self._surface, self._rect)

    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def rect(self) -> Rect:
        return self._rect

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
    def width(self) -> int:
        return self._rect.width

    @width.setter
    @is_value_type(int)
    def width(self, value: int):
        self._rect.width = value

    @property
    def height(self) -> int:
        return self._rect.height

    @height.setter
    @is_value_type(int)
    def height(self, value: int):
        self._rect.height = value

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
    def center(self) -> tuple[int, int]:
        return self._rect.center

    @center.setter
    def center(self, value: tuple[int, int]):
        self._rect.center = value

    @property
    def topleft(self) -> tuple[int, int]:
        return self._rect.topleft

    @topleft.setter
    def topleft(self, value: tuple[int, int]):
        self._rect.topleft = value

    @property
    def topright(self) -> tuple[int, int]:
        return self._rect.topright

    @topright.setter
    def topright(self, value: tuple[int, int]):
        self._rect.topright = value

    @property
    def bottomleft(self) -> tuple[int, int]:
        return self._rect.bottomleft

    @bottomleft.setter
    def bottomleft(self, value: tuple[int, int]):
        self._rect.bottomleft = value

    @property
    def bottomright(self) -> tuple[int, int]:
        return self._rect.bottomright

    @bottomright.setter
    def bottomright(self, value: tuple[int, int]):
        self._rect.bottomright = value

    @property
    def into_top(self) -> int:
        return 0

    @property
    def into_bottom(self) -> int:
        return self.height

    @property
    def into_left(self) -> int:
        return 0

    @property
    def into_right(self) -> int:
        return self.width

    @property
    def into_topleft(self) -> tuple[int, int]:
        return self.into_top, self.into_top

    @property
    def into_topright(self) -> tuple[int, int]:
        return self.into_right, self.into_top

    @property
    def into_bottomleft(self) -> tuple[int, int]:
        return self.into_left, self.into_bottom

    @property
    def into_bottomright(self) -> tuple[int, int]:
        return self.into_right, self.into_bottom

    @property
    def into_centerx(self) -> int:
        return self.width // 2

    @property
    def into_centery(self) -> int:
        return self.height // 2

    @property
    def into_center(self) -> tuple[int, int]:
        return self.into_centerx, self.into_centery
