def is_value_type(types_):
    def decorator(func):
        def wrapper(self, value):
            if isinstance(value, types_):
                func(self, value)
            else:
                raise TypeError(f'Value type have to be {types_}.')

        return wrapper

    return decorator


def is_values_type(*types_):
    def decorator(func):
        def wrapper(self, *args):
            for value, type_ in zip(args, types_):
                if isinstance(value, type_):
                    func(self, value)
                else:
                    raise TypeError(f'Value type have to be {type_}.')

        return wrapper

    return decorator
