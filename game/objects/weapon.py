import pygame
from pygame.sprite import Group

from .projectile import Projectile


class Weapon:
    def __init__(self, projectile: Projectile, projectiles: Group):
        self._projectile = projectile
        self._projectiles = projectiles

    def attack(self):
        new_projectile = Projectile(self._projectile.get_image())
        new_projectile.move_speed = self._projectile.move_speed
        new_projectile.damage = self._projectile.damage
        new_projectile.angle = self._projectile.angle
        new_projectile.center = self._projectile.center
        self._projectiles.add(new_projectile)

    def get_damage(self) -> int:
        return self._projectile.damage

    def set_angle(self, value: int):
        self._projectile.angle = value

    def get_projectile(self) -> Projectile:
        return self._projectile
