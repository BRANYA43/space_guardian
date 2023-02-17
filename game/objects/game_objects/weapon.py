from pygame.sprite import Group

from .projectile import Projectile
from game.utils.decorators import is_values_type
from game.utils.functions import get_valid_value


class Weapon:
    def __init__(self, projectile: Projectile, sprite_group: Group):
        self._projectile: Projectile = get_valid_value(Projectile, projectile)
        self._sprite_group = get_valid_value(sprite_group, Group)

    def get_copy(self):
        return self.create_new_obj(self._projectile, self._sprite_group)

    @classmethod
    def create_new_obj(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @is_values_type(int, int)
    def attack(self, centerx: int, centery: int):
        self._projectile.center = (centerx, centery)
        self._sprite_group.add(self._projectile.get_copy())

    @property
    def projectile(self):
        return self._projectile

