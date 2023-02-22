from pygame import Surface
from pygame.sprite import Sprite

from ..base_objects import GameObject
from .weapon import Weapon
from game.utils.decorators import check_value_type
from game.utils.functions import get_value_with_valid_type
from game.config import LEFT, RIGHT, TILE


class Alien(GameObject, Sprite):
    _global_move_speed = 1
    _global_range_drop = TILE
    _global_moving_left = False
    _global_moving_right = False

    def __init__(self, image: Surface, weapon: Weapon, *, health: int = 0):
        Sprite.__init__(self)
        GameObject.__init__(self, image, health=health)
        self._weapon = get_value_with_valid_type(weapon, Weapon)

    def copy(self):
        return self.create(self.image, self._weapon, health=self.health)

    def update(self):
        if self._global_moving_left:
            self.x -= self._global_move_speed
        if self._global_moving_right:
            self.x += self._global_move_speed

    def drop(self):
        self.y += self._global_range_drop

    @classmethod
    @check_value_type(int)
    def set_global_move_speed(cls, value: int):
        cls._global_move_speed = value

    @classmethod
    @check_value_type(int)
    def set_global_range_drop(cls, value: int):
        cls._global_range_drop = value

    @classmethod
    @check_value_type(int, bool)
    def set_global_moving_flag(cls, direction: int, value: bool):
        if direction == LEFT:
            cls._global_moving_left = value
        elif direction == RIGHT:
            cls._global_moving_right = value
