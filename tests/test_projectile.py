import unittest

from pygame import Surface

from game.objects import Projectile


class TestProjectiles(unittest.TestCase):
    def setUp(self) -> None:
        image = Surface(size=(32, 32))
        self.projectile = Projectile(image)
        self.correct_angle = 10
        self.correct_damage = 10
        self.incorrect_angles = (-1, -1.3, 1.3, '1', 'a', object, [], {}, 360, 1000)
        self.incorrect_damages = (-1, -1.3, 1.3, '1', 'a', object, [], {})

    def test_properties(self):
        # Getters
        self.assertIsInstance(self.projectile.damage, int)
        self.assertIsInstance(self.projectile.angle, int)

        # Setters
        # Correct data
        self.projectile.damage = self.correct_damage
        self.projectile.angle = self.correct_angle

        self.assertEqual(self.correct_damage, self.projectile.damage)
        self.assertEqual(self.correct_angle, self.projectile.angle)

        # Incorrect data
        with self.assertRaises((TypeError, ValueError)):
            for value in self.incorrect_angles:
                self.projectile.angle = value
            for damage in self.incorrect_damages:
                self.projectile.damage = damage

    def test_get_copy(self):
        copy = self.projectile.get_copy()
        self.assertIsNot(self.projectile, copy)
        self.assertEqual(self.projectile.damage, copy.damage)
        self.assertEqual(self.projectile.angle, copy.angle)


if __name__ == '__main__':
    unittest.main()
