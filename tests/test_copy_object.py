import unittest

from game.objects.base_objects import CopyObject


class TestCopyObject(unittest.TestCase):

    def setUp(self) -> None:
        class Obj(CopyObject):
            def __init__(self, text, number):
                super().__init__()
                self.text = text
                self.number = number

            def copy(self):
                return self.create(self.text, self.number)

        self.text = 'text'
        self.number = 1
        self.obj = Obj(self.text, self.number)

    def test_create(self):
        new_obj = self.obj.create(self.text, self.number)
        self.assertIsInstance(new_obj, self.obj.__class__)
        self.assertIsNot(new_obj, self.obj)
        self.assertEqual(self.obj.text, new_obj.text)
        self.assertEqual(self.obj.number, new_obj.number)

    def test_copy(self):
        copy_obj = self.obj.copy()
        self.assertEqual(self.obj.text, copy_obj.text)
        self.assertEqual(self.obj.number, copy_obj.number)


if __name__ == '__main__':
    unittest.main()
