from pygame import Surface

from .weapon import Weapon
from .game_object import GameObject

from game.config import *
from game.global_vairables import *


class Alien(GameObject):
    _move_speed_ = MOVE_SPEED_ALIEN
    _move_speed_down = MOVE_SPEED_DOWN_ALIEN
    _moving_left = False
    _moving_right = False

    def __init__(self, image: Surface, weapon: Weapon):
        super().__init__(image)
        self._weapon = weapon

    def update(self):
        if self._moving_left:
            self.x -= self._move_speed_
        if self._moving_right:
            self.x += self._move_speed_

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
        if direction == LEFT:
            cls._moving_left = value
        elif direction == RIGHT:
            cls._moving_right = value

    def drop(self):
        self.y += self._move_speed_down


