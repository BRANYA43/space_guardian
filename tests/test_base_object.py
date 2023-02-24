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
        # Getters
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

        # Setters
        old_rect = self.obj.rect
        self.obj.surface = Surface((10, 10))
        self.assertIsNot(self.surface, self.obj.surface)

        set_value = 10
        self.obj.x = set_value
        self.assertEqual(set_value, self.obj.x)
        self.obj.y = set_value
        self.assertEqual(set_value, self.obj.y)
        self.obj.top = set_value
        self.assertEqual(set_value, self.obj.top)
        self.obj.bottom = set_value
        self.assertEqual(set_value, self.obj.bottom)
        self.obj.left = set_value
        self.assertEqual(set_value, self.obj.left)
        self.obj.right = set_value
        self.assertEqual(set_value, self.obj.right)
        self.obj.centerx = set_value
        self.assertEqual(set_value, self.obj.centerx)
        self.obj.centery = set_value
        self.assertEqual(set_value, self.obj.centery)

        set_coords = (10, 10)
        self.obj.center = set_coords
        self.assertEqual(set_coords, self.obj.center)
        self.obj.topleft = set_coords
        self.assertEqual(set_coords, self.obj.topleft)
        self.obj.topright = set_coords
        self.assertEqual(set_coords, self.obj.topright)
        self.obj.bottomleft = set_coords
        self.assertEqual(set_coords, self.obj.bottomleft)
        self.obj.bottomright = set_coords
        self.assertEqual(set_coords, self.obj.bottomright)


if __name__ == '__main__':
    unittest.main()
