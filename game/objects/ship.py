import pygame
from pygame.sprite import Group

from game.global_vairables import DIRECTIONS
from .game_object import GameObject
from .weapon import Weapon
from .projectile import Projectile


class Ship(GameObject):
    def __init__(self, image: pygame.Surface):
        super().__init__(image)
        self.move_speed = 5
        self._weapon: Weapon | None = None
        self._health = 1
        self._moving_up = False
        self._moving_down = False
        self._moving_left = False
        self._moving_right = False

    def update(self):
        if self._moving_up:
            self.y -= self.move_speed
        if self._moving_down:
            self.y += self.move_speed
        if self._moving_left:
            self.x -= self.move_speed
        if self._moving_right:
            self.x += self.move_speed

    def set_weapon(self, projectile: Projectile, projectiles: Group):
        self._weapon = Weapon(projectile, projectiles)

    def set_moving_flag(self, direction: int, value: bool):
        self.__setattr__(DIRECTIONS[direction], value)

    def attack(self):
        self._weapon.attack()

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value


