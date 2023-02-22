import re


def check_value_type(*expected_types):
    def decorator(func):
        def wrapper(self, *args):
            for value, expected_type in zip(args, expected_types):
                if not isinstance(value, expected_type):
                    raise TypeError(f'Expected {expected_type}, but got {type(value)}.')
                return func(self, *args)
        return wrapper
    return decorator


def validate_color_code(func):
    def wrapper(self, color_code):
        if not isinstance(color_code, str):
            raise TypeError("Color code have to be a string")
        if not re.match(r"^#[a-fA-F0-9]{6}$", color_code):
            raise ValueError("Invalid color code format")
        return func(self, color_code)
    return wrapper


def validate_coordinates(func):
    def wrapper(self, coordinates):
        if not isinstance(coordinates, tuple):
            raise ValueError("Coordinates have to be a tuple")
        if len(coordinates) != 2:
            raise ValueError("Coordinates have to be a tuple of length 2")
        if not all(isinstance(coord, int) for coord in coordinates):
            raise ValueError("Both coordinates have to be numbers")
        return func(self, coordinates)
    return wrapper
