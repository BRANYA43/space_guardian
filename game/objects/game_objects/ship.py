from pygame import Surface
from pygame.sprite import Group

from ..base_objects import GameObject
from .weapon import Weapon
from game.utils.decorators import is_values_types, is_value_type
from game.utils.functions import get_value_with_valid_type
from game.config import LEFT, RIGHT


class Ship(GameObject):
    def __init__(self, image: Surface, weapon: Weapon, group_projectiles: Group,
                 *, move_speed: int = 5, health: int = 1):
        super().__init__(image, move_speed=move_speed, health=health)
        self._weapon = get_value_with_valid_type(weapon, Weapon)
        self._group_projectiles = get_value_with_valid_type(group_projectiles, Group)
        self._moving_left = False
        self._moving_right = False

    def copy(self):
        pass

    def update(self):
        if self._moving_left:
            self.x -= self.move_speed
        if self._moving_right:
            self.x += self.move_speed

    @is_values_types(int, bool)
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
    @is_value_type(Weapon)
    def weapon(self, value: Weapon):
        self._weapon = value
