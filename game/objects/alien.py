from pygame import Surface

from . import Weapon
from .game_object import GameObject

from game.config import *
from ..global_vairables import *


class Alien(GameObject):
    _move_speed_ = MOVE_SPEED_ALIEN
    _move_speed_down = MOVE_SPEED_DOWN_ALIEN
    _moving_left = False
    _moving_right = False
    _moving_down = False

    def __init__(self, image: Surface, weapon: Weapon):
        super().__init__(image)
        self._weapon = weapon

    def update(self):
        if self._moving_left:
            self.x -= self._move_speed_
        if self._moving_right:
            self.x += self._move_speed_
        if self._moving_down:
            self.y += self._move_speed_down

    def attack(self):
        projectile = self._weapon.get_projectile()
        projectile.centerx = self.centerx
        projectile.top = self.bottom
        self._weapon.attack()

    @property
    def move_speed(self) -> int:
        return self._move_speed_

    @classmethod
    def set_move_speed(cls, value):
        cls._move_speed_ = value

    @classmethod
    def set_moving_flag(cls, direction: int, value: bool):
        directions = {
            DOWN: '_moving_down',
            LEFT: '_moving_left',
            RIGHT: '_moving_right'}
        cls.__setattr__(cls, directions[direction], value)

