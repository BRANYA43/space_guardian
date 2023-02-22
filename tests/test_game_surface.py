import unittest

from pygame import Surface

from game.objects import GameSurface, Projectile


class TestGameSurface(unittest.TestCase):
    def setUp(self) -> None:
        self.image = Surface((32, 32))
        self.obj = GameSurface((100, 100))

    def test_set_color(self):
        self.obj.set_color('#000000')
        self.assertEqual('#000000', self.obj._color)

    def test_set_bg(self):

        self.obj.set_bg(self.image)
        self.assertIs(self.image, self.obj._bg)

    def test_add_blit_object(self):
        self.assertEqual(0, len(self.obj._blit_object_list))
        projectile = Projectile(self.image)
        self.obj.add_blit_object(projectile)
        self.assertEqual(1, len(self.obj._blit_object_list))
        self.assertIs(projectile, self.obj._blit_object_list[0])

    def test_draw(self):
        ...


if __name__ == '__main__':
    unittest.main()
