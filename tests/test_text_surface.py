import unittest

from pygame.font import SysFont

from game.objects import TextSurface


class TestTextSurface(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = TextSurface('')
        self.set_color = '#fff000'

    def test_set_text(self):
        old_surface = self.obj.surface
        old_rect = self.obj.rect
        set_text = 'SomeText'
        self.obj.set_text(set_text)
        self.assertEqual(set_text, self.obj._text)
        self.assertIsNot(old_surface, self.obj.surface)
        self.assertIsNot(old_rect, self.obj.rect)

    def test_set_color(self):
        old_surface = self.obj.surface
        old_rect = self.obj.rect
        self.obj.set_text_color(self.set_color)
        self.assertEqual(self.set_color, self.obj._text_color)
        self.assertIsNot(old_surface, self.obj.surface)
        self.assertIsNot(old_rect, self.obj.rect)

    def test_bg(self):
        old_surface = self.obj.surface
        old_rect = self.obj.rect
        self.obj.set_bg_color(self.set_color)
        self.assertEqual(self.set_color, self.obj._bg_color)
        self.assertIsNot(old_surface, self.obj.surface)
        self.assertIsNot(old_rect, self.obj.rect)

    def test_set_font(self):
        old_font = self.obj._font
        font = SysFont('arial', 14)
        self.obj.set_font(font)
        self.assertIsNot(old_font, self.obj._font)


if __name__ == '__main__':
    unittest.main()
