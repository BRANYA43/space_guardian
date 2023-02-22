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
        self.weapon = Weapon(self.projectile)
        self.alien = Alien(image, self.weapon)

    def test_set_global_move_speed(self):
        self.alien.set_global_move_speed(10)
        self.assertEqual(10, self.alien._global_move_speed)

    def test_set_global_drop(self):
        self.alien.set_global_range_drop(10)
        self.assertEqual(10, self.alien._global_range_drop)

    def test_set_global_moving_flag(self):
        self.assertFalse(self.alien._global_moving_left)
        self.assertFalse(self.alien._global_moving_right)
        self.alien.set_global_moving_flag(RIGHT, True)
        self.assertTrue(self.alien._global_moving_right)
        self.alien.set_global_moving_flag(LEFT, True)
        self.assertTrue(self.alien._global_moving_left)

    def test_update(self):
        set_move_speed = 10
        self.alien.set_global_move_speed(set_move_speed)
        self.alien.x = 0
        self.alien.set_global_moving_flag(RIGHT, True)
        self.alien.set_global_moving_flag(LEFT, False)
        self.alien.update()
        self.assertEqual(set_move_speed, self.alien.x)
        self.alien.update()
        self.assertEqual(set_move_speed * 2, self.alien.x)

        self.alien.x = 0
        self.alien.set_global_moving_flag(RIGHT, False)
        self.alien.set_global_moving_flag(LEFT, True)
        self.alien.update()
        self.assertEqual(-set_move_speed, self.alien.x)
        self.alien.update()
        self.assertEqual(-set_move_speed * 2, self.alien.x)

        self.alien.x = 0
        self.alien.set_global_moving_flag(RIGHT, True)
        self.alien.set_global_moving_flag(LEFT, True)
        self.alien.update()
        self.assertEqual(0, self.alien.x)

    def test_drop(self):
        set_drop = 10
        self.alien.y = 0
        self.alien.set_global_range_drop(set_drop)
        self.alien.drop()
        self.assertEqual(set_drop, self.alien.y)
        self.alien.drop()
        self.assertEqual(set_drop * 2, self.alien.y)

    def test_copy(self):
        copy = self.alien.copy()
        self.assertIsInstance(copy, Alien)
        self.assertIsNot(self.alien, copy)


if __name__ == '__main__':
    unittest.main()
