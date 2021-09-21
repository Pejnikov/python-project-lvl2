from gendiff.difference import get_name, get_value, get_type
from gendiff.difference import has_children, get_new_value
from gendiff.difference import UPDATED, ADDED, REMOVED, Diff
from typing import Dict, List, Any


INDENT = '    '
ADDED_FLAG = '+'
REMOVED_FLAG = '-'
UNMODIFIED_FLAG = ' '
UPDATED_FLAG = '-'
STRINGS_OF_TYPES = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def get_stylish(diffs: List[Diff]) -> str:
    def walk(diffs, cur_indent=''):
        diffs = sorted(diffs, key=get_name)
        result = []
        for diff in diffs:
            type = get_type(diff)
            name = get_name(diff)
            value = get_value(diff)
            new_value = get_new_value(diff)
            if has_children(diff):
                value = walk(value, cur_indent + INDENT)
            result.append(style_diff(cur_indent, type, name, value, new_value))
        result_string = make_result_string('\n'.join(result), cur_indent)
        return result_string
    return walk(diffs)


def style_diff(
    indent: str,
    diff_type: str,
    name: str,
    value: Any,
    new_value: Any
) -> str:
    value = style_value(value, indent)
    new_value = style_value(new_value, indent)
    line = ''
    if diff_type == ADDED:
        line = get_styled_line(indent, ADDED_FLAG, name, value)
    elif diff_type == REMOVED:
        line = get_styled_line(indent, REMOVED_FLAG, name, value)
    elif diff_type == UPDATED:
        line = '\n'.join([
            get_styled_line(indent, REMOVED_FLAG, name, value),
            get_styled_line(indent, ADDED_FLAG, name, new_value)
        ]
        )
    else:
        line = get_styled_line(indent, UNMODIFIED_FLAG, name, value)
    return line


def style_value(value: Any, intend: str) -> str:
    if isinstance(value, dict):
        value = get_styled_dict(value, intend + INDENT)
    elif str(value) in STRINGS_OF_TYPES:
        value = STRINGS_OF_TYPES[str(value)]
    return value


def get_styled_line(indent: str, flag: str, key: str, value: Any) -> str:
    return '{}  {} {}: {}'.format(indent, flag, key, value)


def get_styled_dict(items: Dict, indent: str) -> str:
    sorted_items = sorted(items.items())
    result = []
    for (key, value) in sorted_items:
        if isinstance(value, dict):
            value = get_styled_dict(value, indent + INDENT)
        result.append(get_styled_line(indent, ' ', key, value))
    result_string = make_result_string('\n'.join(result), indent)
    return result_string


def make_result_string(result: str, indent: str) -> str:
    result_string = '{{\n{}\n{}}}'.format(result, indent)
    return result_string
