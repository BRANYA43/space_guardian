from abc import ABC

from pygame import Surface
from pygame.sprite import Sprite


class GameObject(Sprite, ABC):
    def __init__(self, image: Surface):
        super().__init__()
        self._image = image
        self.rect = self._image.get_rect()
        self._move_speed = 0

    @property
    def top(self) -> int:
        return self.rect.top

    @top.setter
    def top(self, value: int):
        self.rect.top = value

    @property
    def bottom(self) -> int:
        return self.rect.bottom

    @bottom.setter
    def bottom(self, value: int):
        self.rect.bottom = value

    @property
    def left(self) -> int:
        return self.rect.left

    @left.setter
    def left(self, value: int):
        self.rect.left = value

    @property
    def right(self) -> int:
        return self.rect.right

    @right.setter
    def right(self, value: int):
        self.rect.right = value

    @property
    def center(self) -> int:
        return self.rect.center

    @center.setter
    def center(self, value: int):
        self.rect.center = value

    @property
    def centerx(self) -> int:
        return self.rect.centerx

    @centerx.setter
    def centerx(self, value: int):
        self.rect.centerx = value

    @property
    def centery(self) -> int:
        return self.rect.centery

    @centery.setter
    def centery(self, value: int):
        self.rect.centery = value

    @property
    def x(self) -> int:
        return self.rect.x

    @x.setter
    def x(self, value: int | float):
        self.rect.x = value

    @property
    def y(self) -> int:
        return self.rect.y

    @y.setter
    def y(self, value: int | float):
        self.rect.y = value

    @property
    def move_speed(self) -> int:
        return self._move_speed

    @move_speed.setter
    def move_speed(self, value: int):
        self._move_speed = value

    def draw(self, surface: Surface):
        surface.blit(self._image, self.rect)

    def update(self):
        if self._move_speed == 0:
            return

    def get_image(self) -> Surface:
        return self._image
