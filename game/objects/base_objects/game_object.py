from abc import ABC

from pygame import Surface

from ..base_objects import CopyObject, BaseObject
from game.utils.decorators import check_value_type
from game.utils.functions import validate_type


class GameObject(BaseObject, CopyObject, ABC):
    def __init__(self, image: Surface, *, move_speed: int = 0, health: int = 0):
        super().__init__(image)
        self._move_speed = validate_type(move_speed, int)
        self._health = validate_type(health, int)

    def copy(self):
        return self.create(self.surface.copy(), move_speed=self._move_speed, health=self._health)

    def update(self):
        if self._move_speed == 0:
            return

    @property
    def image(self):
        return self.surface

    @property
    def move_speed(self) -> int:
        return self._move_speed

    @move_speed.setter
    @check_value_type(int)
    def move_speed(self, value: int):
        if value >= 0:
            self._move_speed = value
        else:
            raise ValueError('Move speed has to be from 0 and over.')

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    @check_value_type(int)
    def health(self, value: int):
        if value >= 0:
            self._health = value
        else:
            raise ValueError('Health has to be from 0 and over.')
