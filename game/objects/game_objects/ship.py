from pygame import Surface

from game.config import *
from ..base_object.game_object import GameObject
from .weapon import Weapon
from game.utils.decorators import is_value_type, is_values_type
from game.utils.functions import get_valid_value


class Ship(GameObject):
    def __init__(self, image: Surface, weapon: Weapon, *, move_speed: int = 5, health: int = 1):
        super().__init__(image, move_speed=move_speed)
        self._weapon = get_valid_value(weapon, Weapon)
        self._health = get_valid_value(health, int)
        self._moving_left = False
        self._moving_right = False

    def get_copy(self):
        return self.create_new_obj(self.image, self._weapon, self.move_speed, self._health)

    def update(self):
        if self._moving_left:
            self.x -= self.move_speed
        if self._moving_right:
            self.x += self.move_speed

    @is_values_type(int, bool)
    def set_moving_flag(self, direction: int, value: bool):
        directions = {
            LEFT: '_moving_left',
            RIGHT: '_moving_right'
        }
        if directions in directions.keys():
            self.__setattr__(directions[direction], value)
        else:
            raise ValueError('Direction has to be LEFT=2 or RIGHT=3.'
                             'Value has to be bool type.')

    def attack(self):
        self._weapon.attack(self.centerx, self.top)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    @is_value_type(int)
    def health(self, value: int):
        if value >= 0:
            self._health = value
        else:
            raise ValueError('Health has be from 0 and bigger.')

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    @is_value_type(Weapon)
    def weapon(self, value: Weapon):
        self._weapon = value
