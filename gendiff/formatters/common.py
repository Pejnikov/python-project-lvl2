STRINGS_OF_TYPES = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def get_type_string(type):
    return STRINGS_OF_TYPES[type]


def need_string(value):
    return isinstance(value, bool) or value is None
