
def validate_type(value, expected_type):
    if not isinstance(value, expected_type):
        raise TypeError(f'Expected {expected_type}, but got {type(value)}.')
    return value
