import unittest

from pygame import Surface, Rect

from game.objects.base_objects.base_object import BaseObject


class TestBaseObject(unittest.TestCase):
    def setUp(self) -> None:
        class Obj(BaseObject):
            def __init__(self, surface: Surface):
                super().__init__(surface)

        self.surface = Surface((100, 50))
        self.obj = Obj(self.surface)

    def test_properties(self):
        property_values = (
            self.obj.x, self.obj.y, self.obj.width, self.obj.height,
            self.obj.top, self.obj.bottom, self.obj.left, self.obj.right,
            self.obj.centerx, self.obj.centery,
            self.obj.into_top, self.obj.into_bottom, self.obj.into_left, self.obj.into_right,
            self.obj.into_centerx, self.obj.into_centery,
            self.obj.center,
            self.obj.topleft, self.obj.topright, self.obj.bottomleft, self.obj.bottomright,
            self.obj.into_topleft, self.obj.into_topright, self.obj.into_bottomleft, self.obj.into_bottomright,
            self.obj.into_center
        )

        correct_values = (0, 0, 100, 50,
                          0, 50, 0, 100,
                          50, 25,
                          0, 50, 0, 100,
                          50, 25,
                          (50, 25),
                          (0, 0), (100, 0), (0, 50), (100, 50),
                          (0, 0), (100, 0), (0, 50), (100, 50),
                          (50, 25))

        self.assertIsInstance(self.obj.surface, Surface)
        self.assertIsInstance(self.obj.rect, Rect)

        for value, correct_value in zip(property_values[:16], correct_values[:16]):
            self.assertIsInstance(value, int)
            self.assertEqual(correct_value, value)

        for value, correct_value in zip(property_values[16:], correct_values[16:]):
            self.assertIsInstance(value, tuple)
            self.assertIsInstance(value[0], int)
            self.assertIsInstance(value[1], int)
            self.assertEqual(correct_value, value)


if __name__ == '__main__':
    unittest.main()
