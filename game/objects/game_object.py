from abc import ABC

from pygame import Surface
from pygame.sprite import Sprite


class GameObject(Sprite, ABC):
    def __init__(self, image: Surface):
        super().__init__()
        self._image = image
        self._rect = self._image.get_rect()
        self._move_speed = 0

    @property
    def top(self) -> int:
        return self._rect.top

    @top.setter
    def top(self, value: int):
        self._rect.top = value

    @property
    def bottom(self) -> int:
        return self._rect.bottom

    @bottom.setter
    def bottom(self, value: int):
        self._rect.bottom = value

    @property
    def left(self) -> int:
        return self._rect.left

    @left.setter
    def left(self, value: int):
        self._rect.left = value

    @property
    def right(self) -> int:
        return self._rect.right

    @right.setter
    def right(self, value: int):
        self._rect.right = value

    @property
    def center(self) -> int:
        return self._rect.center

    @center.setter
    def center(self, value: int):
        self._rect.center = value

    @property
    def centerx(self) -> int:
        return self._rect.centerx

    @centerx.setter
    def centerx(self, value: int):
        self._rect.centerx = value

    @property
    def centery(self) -> int:
        return self._rect.centery

    @centery.setter
    def centery(self, value: int):
        self._rect.centery = value

    @property
    def x(self) -> int:
        return self._rect.x

    @x.setter
    def x(self, value: int | float):
        self._rect.x = value

    @property
    def y(self) -> int:
        return self._rect.y

    @y.setter
    def y(self, value: int | float):
        self._rect.y = value

    @property
    def move_speed(self) -> int:
        return self._move_speed

    @move_speed.setter
    def move_speed(self, value: int):
        self._move_speed = value

    def draw(self, surface: Surface):
        surface.blit(self._image, self._rect)

    def update(self):
        if self._move_speed == 0:
            return

    def get_image(self) -> Surface:
        return self._image
