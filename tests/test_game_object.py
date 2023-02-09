import unittest

from pygame import Surface, Rect

from game.objects.game_object import GameObject


class TestGameObject(unittest.TestCase):
    def setUp(self) -> None:
        image_ = Surface(size=(32, 32))

        class SomeGameObject(GameObject):

            def __init__(self, image):
                super().__init__(image)

            def get_copy(self):
                return super().get_copy()

        self.game_object = SomeGameObject(image_)
        self.correct_data = 1
        self.correct_tuple = (1, 1)
        self.incorrect_data = ('1', 'a', object, 1.3, [], {})

    def test_properties(self):
        # Getters
        self.assertIsInstance(self.game_object.rect, Rect)
        self.assertIsInstance(self.game_object.top, int)
        self.assertIsInstance(self.game_object.bottom, int)
        self.assertIsInstance(self.game_object.left, int)
        self.assertIsInstance(self.game_object.right, int)
        self.assertIsInstance(self.game_object.center, tuple)
        self.assertIsInstance(self.game_object.center[0], int)
        self.assertIsInstance(self.game_object.center[1], int)
        self.assertIsInstance(self.game_object.centerx, int)
        self.assertIsInstance(self.game_object.centery, int)
        self.assertIsInstance(self.game_object.x, int)
        self.assertIsInstance(self.game_object.y, int)
        self.assertIsInstance(self.game_object.move_speed, int)

        # Setters
        # Correct data
        self.game_object.top = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.top)

        self.game_object.bottom = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.bottom)

        self.game_object.left = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.left)

        self.game_object.right = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.right)

        self.game_object.center = self.correct_tuple
        self.assertEqual(self.correct_tuple, self.game_object.center)
        self.assertEqual(self.correct_tuple[0], self.game_object.center[0])
        self.assertEqual(self.correct_tuple[1], self.game_object.center[1])

        self.game_object.centerx = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.centerx)

        self.game_object.centery = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.centery)

        self.game_object.x = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.x)

        self.game_object.y = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.y)

        self.game_object.move_speed = self.correct_data
        self.assertEqual(self.correct_data, self.game_object.move_speed)

        # Incorrect data
        with self.assertRaises(TypeError):
            for value in self.incorrect_data:
                self.game_object.top = value
                self.game_object.bottom = value
                self.game_object.left = value
                self.game_object.right = value
                self.game_object.center = value
                self.game_object.centerx = value
                self.game_object.centery = value
                self.game_object.x = value
                self.game_object.y = value
                self.game_object.move_speed = value

    def test_get_copy(self):
        copy = self.game_object.get_copy()
        self.assertIsInstance(copy, type(self.game_object))
        self.assertIsNot(self.game_object, copy)
        self.assertEqual(self.game_object.x, copy.x)
        self.assertEqual(self.game_object.y, copy.y)
        self.assertEqual(self.game_object.move_speed, copy.move_speed)
        self.assertEqual(self.game_object._image, copy._image)


if __name__ == '__main__':
    unittest.main()












