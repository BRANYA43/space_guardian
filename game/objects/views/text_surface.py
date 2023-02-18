from pygame.font import Font

from game.config import *
from game.fonts import bionicle
from game.utils.decorators import is_value_type
from game.utils.functions import get_valid_value
from game.utils.custom_type import color_code
from game.objects.base_object import BaseObject


class TextSurface(BaseObject):
    def __init__(self, text: str = '', *, font: Font = bionicle, color: color_code = WHITE, bg_color: color_code = None):
        self._text = get_valid_value(text, str)
        self._color = get_valid_value(color, str)
        self._bg_color = get_valid_value(bg_color, str | None)
        self._font: Font = get_valid_value(font, Font)
        super().__init__(self._render())

    @is_value_type(str)
    def set_text(self, value: str):
        self._text = value
        self.surface = self._render()
        self.rect = self.surface.get_rect()

    @is_value_type(color_code)
    def set_color(self, value: color_code):
        self._color = value
        self.surface = self._render()
        self.rect = self.surface.get_rect()

    @is_value_type(color_code)
    def set_bg_color(self, value: color_code):
        self._bg_color = value
        self.surface = self._render()
        self.rect = self.surface.get_rect()

    def _render(self):
        return self._font.render(self._text, False, self._color, self._bg_color)

