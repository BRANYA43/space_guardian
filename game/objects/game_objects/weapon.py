from pygame.sprite import Group

from ..base_objects import CopyObject
from .projectile import Projectile
from game.utils.decorators import check_value_type
from game.utils.functions import validate_type


class Weapon(CopyObject):
    def __init__(self, projectile: Projectile):
        super().__init__()
        self._projectile: Projectile = validate_type(projectile, Projectile)

    def copy(self):
        return self.create(self._projectile.copy())

    @check_value_type(int, int, Group)
    def attack(self, centerx: int, centery: int, projectile_group: Group):
        self._projectile.center = (centerx, centery)
        copy = self._projectile.copy()
        copy.add(projectile_group)

    @property
    def projectile(self):
        return self._projectile
