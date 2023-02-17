from abc import ABC, abstractmethod

from pygame import Surface

from game.objects.base_object import BaseObject
from game.utils.decorators import is_value_type
from game.utils.functions import get_valid_value


class GameObject(BaseObject, ABC):
    def __init__(self, image: Surface, *, move_speed: int = 0):
        super().__init__(image)
        self._move_speed = get_valid_value(int, move_speed)

    def update(self):
        if self._move_speed <= 0:
            return

    @property
    def image(self) -> Surface:
        return self.surface

    @property
    def move_speed(self) -> int:
        return self._move_speed

    @move_speed.setter
    @is_value_type(int)
    def move_speed(self, value: int):
        self._move_speed = value

    @abstractmethod
    def get_copy(self):
        return self.create_new_obj(self.image, move_speed=self._move_speed)

    @classmethod
    def create_new_obj(cls, *args, **kwargs):
        return cls(*args, **kwargs)

