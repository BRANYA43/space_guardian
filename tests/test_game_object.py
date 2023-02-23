import unittest

from pygame import Surface, Rect

from game.objects.base_objects import GameObject


class TestGameObject(unittest.TestCase):
    def setUp(self) -> None:
        class Obj(GameObject):
            def __init__(self, image_, *, move_speed=0, health=0):
                super().__init__(image_, move_speed=move_speed, health=health)

            def copy(self):
                return super().copy()

            def update(self):
                super().update()

        image = Surface((32, 32))
        self.obj = Obj(image)

    def test_properties(self):
        # Getters
        self.assertIsInstance(self.obj.image, Surface)
        self.assertIsInstance(self.obj.move_speed, int)
        self.assertIsInstance(self.obj.health, int)
        self.assertEqual(self.obj.move_speed, 0)
        self.assertEqual(self.obj.health, 0)

        # Setters
        set_value = 100
        self.obj.move_speed = set_value
        self.assertEqual(self.obj.move_speed, set_value)
        self.obj.health = set_value
        self.assertEqual(self.obj.health, set_value)

        with self.assertRaises(ValueError):
            self.obj.move_speed = -123
            self.obj.move_speed -= 123

    def test_copy(self):
        copy = self.obj.copy()
        self.assertIsInstance(copy, self.obj.__class__)
        self.assertIsNot(self.obj, copy)
        self.assertIsNot(self.obj.surface, copy.surface)
        self.assertEqual(self.obj.move_speed, copy.move_speed)
        self.assertEqual(self.obj.health, copy.health)


if __name__ == '__main__':
    unittest.main()












