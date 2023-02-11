import unittest

from pygame import Surface
from pygame.sprite import Group

from game.config import LEFT, RIGHT
from game.objects import Weapon, Projectile
from game.objects import Ship


class TestShip(unittest.TestCase):
    def setUp(self) -> None:
        image = Surface((32, 32))
        self.projectile = Projectile(image)
        self.projectiles = Group()
        self.weapon = Weapon(self.projectile, self.projectiles)
        self.new_weapon = Weapon(self.projectile, self.projectiles)
        self.ship = Ship(image, self.weapon)
        self.correct_health = 10
        self.incorrect_weapon = [1, 1.2, '1', 'das', object]
        self.incorrect_health = [1.2, '1', 'ad', object]
        self.incorrect_flag = ['1', 'adsf', object, 0, 1, 5, 7, 1.2, 2.3]

    def test_properties(self):
        #  Getters
        self.assertIsInstance(self.ship.weapon, Weapon)
        self.assertIs(self.weapon, self.ship.weapon)
        self.assertIsInstance(self.ship.health, int)

        # Setters
        # Correct data
        self.ship.weapon = self.new_weapon
        self.assertIsNot(self.weapon, self.ship.weapon)
        self.ship.health = self.correct_health
        self.assertEqual(self.correct_health, self.ship.health)

        # Incorrect data
        with self.assertRaises((TypeError, ValueError)):
            for data in self.incorrect_weapon:
                self.ship.weapon = data
            for data in self.incorrect_health:
                self.ship.health = data

    def test_set_moving_flag(self):
        self.assertFalse(self.ship._moving_left)
        self.assertFalse(self.ship._moving_right)
        self.ship.set_moving_flag(RIGHT, True)
        self.assertTrue(self.ship._moving_right)
        self.ship.set_moving_flag(LEFT, True)
        self.assertTrue(self.ship._moving_left)

        with self.assertRaises(ValueError):
            for data in self.incorrect_flag:
                print(data)
                self.ship.set_moving_flag(data, True)
                self.ship.set_moving_flag(data, False)

    def test_update(self):
        self.ship.x = 0
        self.ship.move_speed = 5
        self.ship.set_moving_flag(RIGHT, True)
        self.ship.set_moving_flag(LEFT, False)
        for i in range(10):
            self.ship.update()
            self.assertEqual(self.ship.move_speed * (i + 1), self.ship.x)

        self.ship.set_moving_flag(RIGHT, False)
        self.ship.set_moving_flag(LEFT, True)
        for i in range(10):
            self.ship.update()
            self.assertEqual(50 - self.ship.move_speed * (i + 1), self.ship.x)

        for i in range(10):
            self.ship.set_moving_flag(RIGHT, True)
            self.ship.set_moving_flag(LEFT, True)
            self.assertEqual(0, self.ship.x)

    def test_attack(self):
        self.ship.attack()
        projectile = self.projectiles.sprites()[0]
        self.assertIsInstance(projectile, Projectile)
        self.assertIsNot(projectile, self.projectile)
        self.assertEqual(self.ship.centerx, projectile.centerx)
        self.assertEqual(self.ship.top, projectile.centery)


if __name__ == '__main__':
    unittest.main()
