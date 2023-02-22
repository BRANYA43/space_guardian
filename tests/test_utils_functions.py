import unittest

from game.utils.functions import validate_type


class TestUtilsFunctions(unittest.TestCase):
    def test_validate_type(self):
        value = 1
        self.assertEqual(value, validate_type(value, int))
        self.assertEqual(value, validate_type(value, int | str))
        self.assertEqual(str(value), validate_type(str(value), int | str))
        with self.assertRaises(TypeError):
            validate_type(value, str)


if __name__ == '__main__':
    unittest.main()
