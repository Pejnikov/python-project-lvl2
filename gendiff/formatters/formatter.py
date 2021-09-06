from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


FORMATTERS = {
    'stylish': get_stylish,
    'plain': get_plain,
    'json': get_json
}


def get_formater(name):
    if name in FORMATTERS:
        return FORMATTERS[name]
    else:
        raise ValueError

