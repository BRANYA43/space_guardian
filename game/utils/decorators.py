def is_value_type(types_):
    def decorator(func):
        def wrapper(self, value):
            if isinstance(value, types_):
                return func(self, value)
            else:
                raise TypeError(f'Value type have to be {types_}.')

        return wrapper

    return decorator


def is_values_types(*types_):
    def decorator(func):
        def wrapper(self, *args):
            for value, type_ in zip(args, types_):
                if not isinstance(value, type_):
                    raise TypeError(f'Value type have to be {type_}.')
                return func(self, *args)

        return wrapper

    return decorator


def is_color_code(func):
    def wrapper(self, value):
        if not isinstance(value, str) or 7 > len(value) > 7:
            raise ValueError(f'Color has to have format #000000.')
        return func(self, value)

    return wrapper


def is_coordinate(func):
    def wrapper(self, value):
        if not isinstance(value, tuple) \
                or not isinstance(value[0], int) \
                or not isinstance(value[0], int) \
                or len(value) != 2:
            raise ValueError('Coordinate has to be tuple with two argument type of int.')
        return func(self, value)

    return wrapper
