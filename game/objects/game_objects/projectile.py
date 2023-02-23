import math

from pygame import Surface
from pygame.sprite import Sprite

from ..base_objects import GameObject
from game.utils.decorators import check_value_type
from game.utils.functions import validate_type


class Projectile(GameObject, Sprite):
    def __init__(self, image: Surface, *, move_speed: int = 5, health: int = 1, damage: int = 1, angle: int = 270):
        Sprite.__init__(self)
        GameObject.__init__(self, image, move_speed=move_speed, health=health)
        self._damage = validate_type(damage, int)
        self._angle = validate_type(angle, int)

    def copy(self):
        copy = self.create(self.image.copy(),
                           move_speed=self.move_speed,
                           health=self.health,
                           damage=self._damage,
                           angle=self._angle)
        copy.x = self.x
        copy.y = self.y
        return copy

    def update(self):
        radian = self._angle * math.pi / 180
        self.x += round(math.cos(radian) * self.move_speed)
        self.y += round(math.sin(radian) * self.move_speed)

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    @check_value_type(int)
    def damage(self, value: int):
        if value >= 0:
            self._damage = value
        else:
            raise ValueError('Damage has to be from 0 and bigger.')

    @property
    def angle(self) -> int:
        return self._angle

    @angle.setter
    @check_value_type(int)
    def angle(self, value: int):
        if 0 <= value < 360:
            self._angle = value
        else:
            raise ValueError('Angle has to be from 0 to 360.')
