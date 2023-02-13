from pygame import Surface

from .weapon import Weapon
from .ship import Ship

from game.config import *
from game.utils import decorators


class Alien(Ship):
    _global_move_speed = MOVE_SPEED_ALIEN
    _global_range_drop = RANGE_DROP_ALIEN
    _global_moving_left = False
    _global_moving_right = False

    def __init__(self, image: Surface, weapon: Weapon):
        super().__init__(image, weapon)

    def update(self):
        if self._global_moving_left:
            self.x -= self._global_move_speed
        if self._global_moving_right:
            self.x += self._global_move_speed

    def drop(self):
        self.y += self._global_range_drop

    def get_copy(self):
        copy = self._create_obj(self._image, self._weapon)
        copy.health = self._health
        return copy

    def get_global_move_speed(self) -> int:
        return self._global_move_speed

    @classmethod
    @decorators.is_type_value(int)
    def set_global_move_speed(cls, value: int):
        cls._global_move_speed = value

    def get_global_range_drop(self) -> int:
        return self._global_range_drop

    @classmethod
    @decorators.is_type_value(int)
    def set_global_range_drop(cls, value: int):
        cls._global_range_drop = value

    @classmethod
    def set_global_moving_flag(cls, direction: int, value: bool):
        if direction == LEFT:
            cls._global_moving_left = value
        elif direction == RIGHT:
            cls._global_moving_right = value
        else:
            raise ValueError('Direction has to be LEFT=2 or RIGHT=3.'
                             'Value has to be bool type.')
