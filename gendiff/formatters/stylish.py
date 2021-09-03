from gendiff.difference import get_name, get_value, get_type, DIFF_TYPES
from gendiff.difference import has_children, get_new_value


INDENT = '    '
DIFF_ID = {
    DIFF_TYPES['ADDED']: '+',
    DIFF_TYPES['REMOVED']: '-',
    DIFF_TYPES['UNMODIFIED']: ' ',
    DIFF_TYPES['UPDATED']: '-',
}


def get_stylish(diffs):
    def walk(diffs, cur_indent=''):
        result = ''
        for diff in diffs:
            type = get_type(diff)
            name = get_name(diff)
            value = get_value(diff)
            new_value = get_new_value(diff)
            if has_children(diff):
                value = walk(value, cur_indent + INDENT)
            result += style_string(cur_indent, type, name, value, new_value)
        result = make_result_string(result, cur_indent)
        return result
    return walk(diffs)


def style_string(indent, diff_type, name, value, new_value):
    value = format_value(value, indent)
    new_value = format_value(new_value, indent)
    result = format_string(indent, DIFF_ID[diff_type], name, value)
    if diff_type is DIFF_TYPES['UPDATED']:
        result += format_string(indent, DIFF_ID['ADDED'], name, new_value)
    return result


def format_value(value, intend):
    if isinstance(value, dict):
        value = get_formatted_dict(value, intend + INDENT)
    value = format_python_types(value)
    return value


def format_string(indent, flag, key, value):
    return '{}  {} {}: {}\n'.format(indent, flag, key, value)


def get_formatted_dict(items, indent):
    sorted_items = sorted(items.items())
    result = ''
    for (key, value) in sorted_items:
        if isinstance(value, dict):
            value = get_formatted_dict(value, indent + INDENT)
        result += format_string(indent, ' ', key, value)
    result = make_result_string(result, indent)
    return result


def make_result_string(result, indent):
    result_string = '{{\n{}{}}}'.format(result, indent)
    return result_string


def format_python_types(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value
