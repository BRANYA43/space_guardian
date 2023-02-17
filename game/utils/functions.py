def get_valid_value(value, types_):
    if isinstance(value, types_):
        return value
    else:
        raise TypeError(f'Value type have to be {types_}.')
