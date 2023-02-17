from pygame import Surface

from .weapon import Weapon
from .ship import Ship

from game.config import *
from game.utils.decorators import is_value_type, is_values_type


class Alien(Ship):
    _global_move_speed = 1
    _global_range_drop = TILE
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
        return self.create_new_obj(self.image, self.weapon, self.health)

    @classmethod
    @is_value_type(int)
    def set_global_move_speed(cls, value: int):
        cls._global_move_speed = value

    @classmethod
    @is_value_type(int)
    def set_global_range_drop(cls, value: int):
        cls._global_range_drop = value

    @classmethod
    @is_values_type(int, bool)
    def set_global_moving_flag(cls, direction: int, value: bool):
        if direction == LEFT:
            cls._global_moving_left = value
        elif direction == RIGHT:
            cls._global_moving_right = value
        else:
            raise ValueError('Direction has to be LEFT=2 or RIGHT=3.'
                             'Value has to be bool type.')
