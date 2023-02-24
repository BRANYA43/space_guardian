import unittest

from game.objects import TextSurface
from game.objects.base_objects.widget import Widget


class TestWidget(unittest.TestCase):
    def setUp(self) -> None:
        class Obj(Widget):
            def __init__(self):
                super().__init__('Test', '0')

        self.obj = Obj()

    def test_properties(self):
        self.assertIsInstance(self.obj.title, TextSurface)
        self.assertIsInstance(self.obj.value, TextSurface)

    def test_get_blits(self):
        blits = self.obj.get_blits()
        self.assertIsInstance(blits, tuple)
        self.assertIsInstance(blits[0], TextSurface)
        self.assertIsInstance(blits[1], TextSurface)

    def test_set_value(self):
        ...

    def test_color(self):
        ...


if __name__ == '__main__':
    unittest.main()
