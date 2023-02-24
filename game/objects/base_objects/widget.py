from abc import ABC
from typing import Tuple

from game.objects import TextSurface
from game.utils.decorators import validate_color_code


class Widget(ABC):
    def __init__(self, title: str, value: str):
        self._title = TextSurface(title)
        self._value = TextSurface(value)

    def get_blits(self) -> tuple[TextSurface, ...]:
        return self._title, self._value

    @property
    def title(self) -> TextSurface:
        return self._title

    @property
    def value(self) -> TextSurface:
        return self._value

    def draw(self, surface):
        self._title.draw(surface)
        self._value.draw(surface)

    def set_value(self, value: str):
        self._value.set_text(value)

    @validate_color_code
    def set_color(self, color: str):
        self._title.set_text_color(color)
        self._value.set_text_color(color)
