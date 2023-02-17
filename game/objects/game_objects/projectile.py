import math

from pygame import Surface
from pygame.sprite import Sprite

from ..base_object.game_object import GameObject
from game.utils.decorators import is_value_type
from game.utils.functions import get_valid_value


class Projectile(GameObject, Sprite):
    def __init__(self, image: Surface, *, move_speed: int = 5, damage: int = 1, angle: int = 270):
        Sprite.__init__(self)
        GameObject.__init__(self, image, move_speed=move_speed)
        self._damage = get_valid_value(damage, int)
        self._angle = get_valid_value(angle, int)

    def get_copy(self):
        return self.create_new_obj(self.image, move_speed=self.move_speed, damage=self._damage, agnle=self._angle)

    def update(self):
        radian = self._angle * math.pi / 180
        self.x += round(math.cos(radian) * self.move_speed)
        self.y += round(math.sin(radian) * self.move_speed)

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    @is_value_type(int)
    def damage(self, value: int):
        if value >= 0:
            self._damage = value
        else:
            raise ValueError('Damage has to be from 0 and bigger. Damage >= 0.')

    @property
    def angle(self) -> int:
        return self._angle

    @angle.setter
    @is_value_type(int)
    def angle(self, value: int):
        if 0 <= value < 360:
            self._angle = value
        else:
            raise ValueError('Angle has to be from/equal 0 and smaller 360. 0 >= Angle < 360')
