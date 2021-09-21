from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json
from typing import Callable

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
FORMATTERS = {
    STYLISH: get_stylish,
    PLAIN: get_plain,
    JSON: get_json
}


def get_formater(name: str) -> Callable:
    if name in FORMATTERS:
        return FORMATTERS[name]
    else:
        raise ValueError
