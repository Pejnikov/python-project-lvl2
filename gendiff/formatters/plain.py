from gendiff.difference import get_name, get_value, get_type, get_new_value
from gendiff.difference import has_children, ADDED, REMOVED, UNMODIFIED
from gendiff.difference import UPDATED
from typing import Tuple, List, Any

PATH_DIVIDER = '.'
STRINGS_OF_TYPES = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def get_plain(diffs: List[Tuple[str, str, Any, Any]]) -> str:
    def walk(diffs, name):
        diffs = sorted(diffs, key=get_name)
        result = []
        for diff in diffs:
            diff_type = get_type(diff)
            cur_name = name + get_name(diff)
            value = get_value(diff)
            new_value = get_new_value(diff)
            if has_children(diff):
                children_string = walk(value, cur_name + PATH_DIVIDER)
                result.append(children_string)
                continue
            if diff_type is UNMODIFIED:
                continue
            main_line = plain_line(diff_type, cur_name, value, new_value)
            result.append(main_line)
        return '\n'.join(result)
    return walk(diffs, name='')


def plain_line(diff_type: str, name: str, value: Any, new_value: Any) -> str:
    result = ''
    value = format_value(value)
    new_value = format_value(new_value)
    if diff_type is ADDED:
        result = f"Property '{name}' was added with value: {value}"
    elif diff_type is REMOVED:
        result = f"Property '{name}' was removed"
    elif diff_type is UPDATED:
        result = f"Property '{name}' was updated. From {value} to {new_value}"
    return result


def format_value(value: Any) -> Any:
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, str):
        return "'{}'".format(value)
    elif str(value) in STRINGS_OF_TYPES:
        return STRINGS_OF_TYPES[str(value)]
    else:
        return value
