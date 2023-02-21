from pygame import display

from ..base_objects import BaseObject


class Display(BaseObject):
    def __init__(self, size: tuple[int, int]):
        super().__init__(display.set_mode(size))

    @property
    def display(self):
        return self.surface

