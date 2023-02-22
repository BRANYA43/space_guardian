from pygame import Surface
from pygame.font import Font

from ..base_objects import BaseObject
from game.config import *
from game.fonts import bionicle
from game.utils.decorators import check_value_type, validate_color_code
from game.utils.functions import validate_type


class TextSurface(BaseObject):
    def __init__(self, text: str, *, font: Font = bionicle, color: str = WHITE, bg: Surface = None):
        self._text = validate_type(text, str)
        self._text_color = validate_type(color, str)
        self._font: Font = validate_type(font, Font)
        self._bg_color = validate_type(bg, str | None)
        super().__init__(self._render())

    def _render(self) -> Surface:
        self.surface = self._font.render(self._text, False, self._text_color, self._bg_color)
        return self.surface

    @check_value_type(str)
    def set_text(self, value: str):
        self._text = value
        self._render()

    @validate_color_code
    def set_text_color(self, value: str):
        self._text_color = value
        self._render()

    @validate_color_code
    def set_bg_color(self, value: str):
        self._bg_color = value
        self._render()

    @check_value_type(Font)
    def set_font(self, value: Font):
        self._font = value
        self._render()
