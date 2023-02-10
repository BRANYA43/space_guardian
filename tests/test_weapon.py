import unittest

from pygame import Surface
from pygame.sprite import Group

from game.objects import Weapon, Projectile


class TestWeapon(unittest.TestCase):
    def setUp(self) -> None:
        image = Surface((32, 32))
        self.projectile = Projectile(image)
        self.projectiles = Group()
        self.weapon = Weapon(self.projectile, self.projectiles)
        self.correct_center = (10, 10)
        self.correct_angle = 100

    def test_properties(self):
        self.assertIsInstance(self.weapon.projectile, Projectile)
        self.assertIs(self.projectile, self.weapon.projectile)

    def test_copy(self):
        copy = self.weapon.get_copy()
        self.assertIsInstance(copy, Weapon)
        self.assertIsNot(self.weapon, copy)
        self.assertIs(self.projectile, self.weapon.projectile)
        self.assertIs(self.projectiles, self.weapon._projectiles)

    def test_attack(self):
        self.weapon.attack(*self.correct_center)
        self.assertEqual(self.correct_center[0], self.weapon.projectile.centerx)
        self.assertEqual(self.correct_center[1], self.weapon.projectile.centery)

    def test_set_attack_angle(self):
        self.weapon.set_attack_angle(self.correct_angle)
        self.assertEqual(self.correct_angle, self.weapon.projectile.angle)


if __name__ == '__main__':
    unittest.main()
