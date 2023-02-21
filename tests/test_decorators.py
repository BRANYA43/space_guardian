import unittest

from game.utils.decorators import *


class TestDecorators(unittest.TestCase):
    def setUp(self) -> None:
        class Obj:
            @is_value_type(int)
            def func0(self, v):
                return v

            @is_values_types(int, str, object)
            def func1(self, v1, v2, v3):
                return v1, v2, v3

            @is_coordinate
            def func2(self, v):
                return v

            @is_color_code
            def func3(self, v):
                return v

        self.obj = Obj()

    def test_is_value_type(self):
        self.assertEqual(1, self.obj.func0(1))
        with self.assertRaises(TypeError):
            self.obj.func0('1')

    def test_is_values_types(self):
        values = (1, '1', object)
        self.assertEqual(values, self.obj.func1(*values))
        with self.assertRaises(TypeError):
            self.obj.func1(1, [], object)
            self.obj.func1([], [], [])

    def test_is_coordinate(self):
        coord = (1, 1)
        self.assertEqual(coord, self.obj.func2(coord))
        with self.assertRaises(ValueError):
            self.obj.func2(1)
            self.obj.func2('1')
            self.obj.func2((1, '1'))
            self.obj.func2(('1', '1'))
            self.obj.func2(())

    def test_is_color(self):
        color = '#000000'
        self.assertEqual(color, self.obj.func3(color))
        with self.assertRaises(ValueError):
            self.obj.func3('')
            self.obj.func3('#000')
            self.obj.func3(1)


if __name__ == '__main__':
    unittest.main()
