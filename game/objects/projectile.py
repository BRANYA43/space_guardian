import math

from pygame import Surface

from .game_object import GameObject
from game.utils import decorators


class Projectile(GameObject):
    def __init__(self, image: Surface):
        super().__init__(image)
        self.move_speed = 5
        self._damage = 1
        self._angle = 270

    def update(self):
        radian = self._angle * math.pi / 180
        self.x += round(math.cos(radian) * self.move_speed)
        self.y += round(math.sin(radian) * self.move_speed)

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    @decorators.is_type_value(int)
    def damage(self, value: int):
        if value >= 0:
            self._damage = value
        else:
            raise ValueError('Damage has to be from 0 and bigger.')

    @property
    def angle(self) -> int:
        return self._angle

    @angle.setter
    @decorators.is_type_value(int)
    def angle(self, value: int):
        if 0 <= value < 360:
            self._angle = value
        else:
            raise ValueError('Angle has to be from/equal 0 and smaller 360.')

    def get_copy(self):
        copy = super().get_copy()
        copy.damage = self.damage
        copy.angle = self._angle
        return copy



