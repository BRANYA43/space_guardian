from pygame import Surface

from game.config import *
from .base_objects import GameObject
from .weapon import Weapon
from game.utils import decorators


class Ship(GameObject):
    def __init__(self, image: Surface, weapon: Weapon):
        super().__init__(image)
        self.move_speed = 5
        self._weapon = weapon
        self._health = 1
        self._moving_left = False
        self._moving_right = False

    def get_copy(self):
        copy = self._create_obj(self._image, self._weapon)
        copy.health = self._health
        copy.move_speed = self.move_speed
        return copy

    def update(self):
        if self._moving_left:
            self.x -= self.move_speed
        if self._moving_right:
            self.x += self.move_speed

    def set_moving_flag(self, direction: int, value: bool):
        directions = {
            LEFT: '_moving_left',
            RIGHT: '_moving_right'
        }
        if direction in directions.keys() and type(value) is bool:
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
    @decorators.is_type_value(int)
    def health(self, value: int):
        if value >= 0:
            self._health = value
        else:
            raise ValueError('Health has be from 0 and bigger.')

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    @decorators.is_type_value(Weapon)
    def weapon(self, value: Weapon):
        self._weapon = value
