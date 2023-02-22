import unittest

from game.utils.decorators import *


class TestDecorators(unittest.TestCase):
    def setUp(self) -> None:
        class Obj:
            @check_value_type(int)
            def check_value_type_func1(self, v):
                return v

            @check_value_type(int | str)
            def check_value_type_func2(self, v):
                return v

            @check_value_type(int, str)
            def check_value_type_func3(self, v1, v2):
                return v1, v2

            @check_value_type(int, str | object)
            def check_value_type_func4(self, v1, v2):
                return v1, v2

            @validate_coordinates
            def validate_coordinates_func(self, v):
                return v

            @validate_color_code
            def validate_color_code_func(self, v):
                return v

        self.obj = Obj()

    def test_check_value_type(self):
        self.assertEqual(1, self.obj.check_value_type_func1(1))

        self.assertEqual(1, self.obj.check_value_type_func2(1))
        self.assertEqual('1', self.obj.check_value_type_func2('1'))

        self.assertEqual((1, '1'), self.obj.check_value_type_func3(1, '1'))

        self.assertEqual((1, '1'), self.obj.check_value_type_func4(1, '1'))
        self.assertEqual((1, object), self.obj.check_value_type_func4(1, object))

        with self.assertRaises(TypeError):
            self.obj.check_value_type_func1(None)
            self.obj.check_value_type_func2(None)
            self.obj.check_value_type_func3(1, None)
            self.obj.check_value_type_func3(None, '1')
            self.obj.check_value_type_func3(None, None)
            self.obj.check_value_type_func4(1, None)
            self.obj.check_value_type_func4(None, '1')
            self.obj.check_value_type_func4(None, object)
            self.obj.check_value_type_func4(None, None)

    def test_validate_coordinates(self):
        self.assertEqual((1, 1), self.obj.validate_coordinates_func((1, 1)))

        with self.assertRaises((TypeError, ValueError)):
            self.obj.validate_coordinates_func(1, 1)
            self.obj.validate_coordinates_func((1, 1, 1))
            self.obj.validate_coordinates_func((1,))
            self.obj.validate_coordinates_func((None, 1))
            self.obj.validate_coordinates_func((1, None))
            self.obj.validate_coordinates_func((None, None))

    def test_is_color(self):
        self.assertEqual('#000000', self.obj.validate_color_code_func('#000000'))

        with self.assertRaises((TypeError, ValueError)):
            self.obj.validate_color_code_func(None)
            self.obj.validate_color_code_func('#/*-*/-')
            self.obj.validate_color_code_func('#/*-')
            self.obj.validate_color_code_func('000000')


if __name__ == '__main__':
    unittest.main()
