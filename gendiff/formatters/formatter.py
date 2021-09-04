from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain


def get_formater(name):
    if name == 'plain':
        return get_plain
    if name == 'stylish':
        return get_stylish
    else:
        raise ValueError
