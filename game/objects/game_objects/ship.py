from pygame import Surface
from pygame.sprite import Group

from ..base_objects import GameObject
from .weapon import Weapon
from game.utils.decorators import check_value_type
from game.utils.functions import validate_type
from game.config import LEFT, RIGHT


class Ship(GameObject):
    def __init__(self, image: Surface, weapon: Weapon, group_projectiles: Group,
                 *, move_speed: int = 5, health: int = 1):
        super().__init__(image, move_speed=move_speed, health=health)
        self._weapon = validate_type(weapon, Weapon)
        self._group_projectiles = validate_type(group_projectiles, Group)
        self._moving_left = False
        self._moving_right = False

    def copy(self):
        pass

    def update(self):
        if self._moving_left:
            self.x -= self.move_speed
        if self._moving_right:
            self.x += self.move_speed

    @check_value_type(int, bool)
    def set_moving_flag(self, direction: int, value: bool):
        directions = {
            LEFT: '_moving_left',
            RIGHT: '_moving_right'
        }
        self.__setattr__(directions[direction], value)

    def attack(self):
        self._weapon.attack(self.centerx, self.top, self._group_projectiles)

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    @check_value_type(Weapon)
    def weapon(self, value: Weapon):
        self._weapon = value
