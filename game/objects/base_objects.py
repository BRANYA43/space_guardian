from abc import ABC, abstractmethod

from pygame import Surface, Rect
from pygame.sprite import Sprite

from game.utils import decorators, functions


class BaseObject(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        """Initialization parameters"""
        pass

    @abstractmethod
    def get_copy(self):
        """Gets a copy object"""
        pass

    @classmethod
    def _create_obj(cls, *args, **kwargs):
        """Creates and gets copy objects"""
        return cls(*args, **kwargs)


class GameObject(BaseObject, Sprite, ABC):
    @abstractmethod
    def __init__(self, image: Surface):
        super().__init__()
        self._image = functions.get_valid_value(Surface, image)
        self._rect = self._image.get_rect()
        self._move_speed = 0

    def draw(self, surface: Surface):
        surface.blit(self._image, self._rect)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_copy(self):
        copy = self._create_obj(self._image)
        copy.move_speed = self._move_speed
        copy.x = self._rect.x
        copy.y = self._rect.y
        return copy

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def top(self) -> int:
        return self._rect.top

    @top.setter
    @decorators.is_type_value(int)
    def top(self, value: int):
        self._rect.top = value

    @property
    def bottom(self) -> int:
        return self._rect.bottom

    @bottom.setter
    @decorators.is_type_value(int)
    def bottom(self, value: int):
        self._rect.bottom = value

    @property
    def left(self) -> int:
        return self._rect.left

    @left.setter
    @decorators.is_type_value(int)
    def left(self, value: int):
        self._rect.left = value

    @property
    def right(self) -> int:
        return self._rect.right

    @right.setter
    @decorators.is_type_value(int)
    def right(self, value: int):
        self._rect.right = value

    @property
    def center(self) -> tuple[int, int]:
        return self._rect.center

    @center.setter
    @decorators.is_type_value(tuple)
    def center(self, value: tuple):
        self._rect.center = value

    @property
    def centerx(self) -> int:
        return self._rect.centerx

    @centerx.setter
    @decorators.is_type_value(int)
    def centerx(self, value: int):
        self._rect.centerx = value

    @property
    def centery(self) -> int:
        return self._rect.centery

    @centery.setter
    @decorators.is_type_value(int)
    def centery(self, value: int):
        self._rect.centery = value

    @property
    def x(self) -> int:
        return self._rect.x

    @x.setter
    @decorators.is_type_value(int)
    def x(self, value: int):
        self._rect.x = value

    @property
    def y(self) -> int:
        return self._rect.y

    @y.setter
    @decorators.is_type_value(int)
    def y(self, value: int):
        self._rect.y = value

    @property
    def move_speed(self) -> int:
        return self._move_speed

    @move_speed.setter
    @decorators.is_type_value(int)
    def move_speed(self, value: int):
        self._move_speed = value
