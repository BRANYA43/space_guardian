def get_valid_value(type_, value):
    if type(value) is type_:
        return value
    else:
        raise TypeError(f'Value type have to be {type_}.')
