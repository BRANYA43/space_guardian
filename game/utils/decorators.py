def is_type_value(type_):
    def decorator(func):
        def wrapper(self, value):
            if type(value) is type_:
                func(self, value)
            else:
                raise TypeError(f'Value type have to be {type_}.')
        return wrapper
    return decorator
