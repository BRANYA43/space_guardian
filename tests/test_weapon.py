import unittest

from pygame import Surface
from pygame.sprite import Group

from game.objects import Weapon, Projectile


class TestWeapon(unittest.TestCase):
    def setUp(self) -> None:
        image = Surface((32, 32))
        self.projectile = Projectile(image)
        self.obj = Weapon(self.projectile)

    def test_properties(self):
        self.assertIsInstance(self.obj.projectile, Projectile)
        self.assertIs(self.projectile, self.obj.projectile)

    def test_copy(self):
        copy = self.obj.copy()
        self.assertIsInstance(copy, Weapon)
        self.assertIsNot(self.obj, copy)
        self.assertIsInstance(copy.projectile, Projectile)
        self.assertIsNot(self.obj.projectile, copy.projectile)

    def test_attack(self):
        projectile_group = Group()
        set_coord = (10, 10)
        self.assertEqual((16, 16), self.projectile.center)
        self.assertEqual(0, len(projectile_group.sprites()))
        self.obj.attack(*set_coord, projectile_group)
        self.assertEqual(set_coord, self.projectile.center)
        self.assertEqual(1, len(projectile_group.sprites()))


if __name__ == '__main__':
    unittest.main()
