from pygame.sprite import Group

from .game_object import GameObject1
from .projectile import Projectile
from game.utils import functions


class Weapon(GameObject1):
    def __init__(self, projectile: Projectile, projectiles: Group):
        self._projectile: Projectile = functions.get_valid_value(Projectile, projectile)
        self._projectiles = functions.get_valid_value(Group, projectiles)

    def get_copy(self):
        copy = self._create_obj(self._projectile, self._projectiles)
        return copy

    def attack(self, centerx: int, centery: int):
        self._projectile.center = (centerx, centery)
        self._projectiles.add(self._projectile.get_copy())

    @property
    def projectile(self):
        return self._projectile

    def set_attack_angle(self, value: int):
        self._projectile.angle = value
