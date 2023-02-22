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
        self.weapon = Weapon(self.projectile)
        self.projectile_group = Group()
        self.ship = Ship(image, self.weapon, self.projectile_group)

    def test_properties(self):
        #  Getters
        self.assertIsInstance(self.ship.weapon, Weapon)

        # Setters
        self.ship.weapon = Weapon(self.projectile)
        self.assertIsNot(self.weapon, self.ship.weapon)

    def test_set_moving_flag(self):
        self.assertFalse(self.ship._moving_left)
        self.assertFalse(self.ship._moving_right)
        self.ship.set_moving_flag(RIGHT, True)
        self.assertTrue(self.ship._moving_right)
        self.ship.set_moving_flag(LEFT, True)
        self.assertTrue(self.ship._moving_left)

    def test_update(self):
        self.ship.x = 0
        self.ship.move_speed = 10
        self.ship.set_moving_flag(RIGHT, True)
        self.ship.set_moving_flag(LEFT, False)
        self.ship.update()
        self.assertEqual(self.ship.move_speed, self.ship.x)
        self.ship.update()
        self.assertEqual(self.ship.move_speed * 2, self.ship.x)

        self.ship.x = 0
        self.ship.set_moving_flag(RIGHT, False)
        self.ship.set_moving_flag(LEFT, True)
        self.ship.update()
        self.assertEqual(-self.ship.move_speed, self.ship.x)
        self.ship.update()
        self.assertEqual(-self.ship.move_speed * 2, self.ship.x)

        self.ship.x = 0
        self.ship.set_moving_flag(RIGHT, True)
        self.ship.set_moving_flag(LEFT, True)
        self.ship.update()
        self.assertEqual(0, self.ship.x)

    def test_attack(self):
        self.assertEqual(0, len(self.projectile_group.sprites()))
        self.ship.attack()
        self.assertEqual(1, len(self.projectile_group.sprites()))
        projectile = self.projectile_group.sprites()[0]
        self.assertEqual(self.ship.centerx, projectile.centerx)
        self.assertEqual(self.ship.top, projectile.centery)


if __name__ == '__main__':
    unittest.main()
