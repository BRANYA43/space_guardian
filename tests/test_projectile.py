import unittest

from pygame import Surface

from game.objects import Projectile


class TestProjectiles(unittest.TestCase):
    def setUp(self) -> None:
        image = Surface((32, 32))
        self.obj = Projectile(image)

    def test_properties(self):
        # Getters
        self.assertIsInstance(self.obj.damage, int)
        self.assertIsInstance(self.obj.angle, int)

        # Setters
        set_value = 100
        self.obj.damage = set_value
        self.assertEqual(set_value, self.obj.damage)
        self.obj.angle = set_value
        self.assertEqual(set_value, self.obj.angle)

        with self.assertRaises(ValueError):
            self.obj.damage = -1
            self.obj.angle = -1
            self.obj.angle = 360
            self.obj.angle = 1000

    def test_update(self):
        self.obj.angle = 90
        self.obj.move_speed = 10
        self.obj.update()
        self.assertEqual(0, self.obj.x)
        self.assertEqual(self.obj.move_speed, self.obj.y)
        self.obj.update()
        self.assertEqual(0, self.obj.x)
        self.assertEqual(self.obj.move_speed * 2, self.obj.y)

    def test_copy(self):
        copy = self.obj.copy()
        self.assertIsInstance(copy, self.obj.__class__)
        self.assertIsNot(self.obj, copy)
        self.assertIsNot(self.obj.surface, copy.surface)
        self.assertEqual(self.obj.move_speed, copy.move_speed)
        self.assertEqual(self.obj.health, copy.health)
        self.assertEqual(self.obj.damage, copy.damage)
        self.assertEqual(self.obj.angle, copy.angle)


if __name__ == '__main__':
    unittest.main()
