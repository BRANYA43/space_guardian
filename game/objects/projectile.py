import math

from pygame import Surface

from game_object import GameObject


class Projectile(GameObject):
    def __init__(self, image: Surface):
        super().__init__(image)
        self._move_speed = 5
        self._damage = 1
        self._angle = 270
        
    def update(self):
        radian = self._angle * math.pi / 180
        self._rect.x += round(math.cos(radian) * self._move_speed)
        self._rect.y += round(math.sin(radian) * self._move_speed)
    
    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, value: int):
        self._damage = value
    
    @property
    def angle(self) -> int:
        return self._angle
    
    @angle.setter
    def angle(self, value: int):
        self._angle = value
