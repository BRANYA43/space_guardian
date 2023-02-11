import unittest

from pygame import Surface
from pygame.sprite import Group

from game.config import RIGHT, LEFT
from game.objects import Alien, Weapon, Projectile


class TestAlien(unittest.TestCase):
    def setUp(self) -> None:
        image = Surface((32, 32))
        self.projectile = Projectile(image)
        self.projectiles = Group()
        self.weapon = Weapon(self.projectile, self.projectiles)
        self.alien = Alien(image, self.weapon)
        self.correct_range_drop = 100
        self.correct_move_speed = 100
        self.incorrect_data = ('1', 'sd', 1.2, object)

    def test_properties(self):
        # Getters
        self.assertIsInstance(self.alien.get_global_move_speed(), int)
        self.assertIsInstance(self.alien.get_global_range_drop(), int)

        # Setters
        # Correct data
        self.alien.set_global_move_speed(self.correct_move_speed)
        self.assertEqual(self.correct_move_speed, self.alien.get_global_move_speed())

        self.alien.set_global_range_drop(self.correct_range_drop)
        self.assertEqual(self.correct_range_drop, self.alien.get_global_range_drop())

        # Incorrect data
        with self.assertRaises(TypeError):
            for data in self.incorrect_data:
                self.alien.set_global_move_speed(data)
                self.alien.set_global_range_drop(data)

    def test_update(self):
        self.alien.x = 0
        self.alien.set_global_move_speed(5)
        self.alien.set_global_moving_flag(RIGHT, True)
        self.alien.set_global_moving_flag(LEFT, False)
        for i in range(10):
            self.alien.update()
            self.assertEqual(self.alien.get_global_move_speed() * (i + 1), self.alien.x)

        self.alien.set_global_moving_flag(RIGHT, False)
        self.alien.set_global_moving_flag(LEFT, True)
        for i in range(10):
            self.alien.update()
            self.assertEqual(50 - self.alien.get_global_move_speed() * (i + 1), self.alien.x)

    def test_drop(self):
        self.alien.y = 0
        self.alien.set_global_range_drop(5)
        for i in range(10):
            self.alien.drop()
            self.assertEqual(self.alien.get_global_range_drop() * (i + 1), self.alien.y)


if __name__ == '__main__':
    unittest.main()
