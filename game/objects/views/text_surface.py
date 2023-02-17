from pygame.font import SysFont

from game.config import *
from game.utils.decorators import is_value_type, is_values_type
from game.utils.functions import get_valid_value
from game.utils.custom_type import color_code
from game.objects.base_object import BaseObject


class TextSurface(BaseObject):
    def __init__(self, text: str = '', *, font_name: str = FONT_NAME, font_size: int = FONT_SIZE,
                 color: color_code = WHITE, bg_color: color_code = None):
        self.text = get_valid_value(text, str)
        self.color = get_valid_value(color, color_code)
        self.bg_color = get_valid_value(bg_color, color_code)
        self.set_font(font_name, font_size)
        super().__init__(self._render())

    @is_value_type(str)
    def set_text(self, value: str):
        self.text = value
        self.surface = self._render()
        self.rect = self.surface.get_rect()

    @is_value_type(color_code)
    def set_color(self, value: color_code):
        self.color = value
        self.surface = self._render()
        self.rect = self.surface.get_rect()

    @is_value_type(color_code)
    def set_bg_color(self, value: color_code):
        self.bg_color = value
        self.surface = self._render()
        self.rect = self.surface.get_rect()

    @is_values_type(str, int)
    def set_font(self, name: str, size: int):
        self.font = SysFont(name, size)

    def _render(self):
        return self.font.render(self.text, False, self.color, self.bg_color)

