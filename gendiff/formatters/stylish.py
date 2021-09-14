from gendiff.difference import get_name, get_value, get_type
from gendiff.difference import has_children, get_new_value
from gendiff.difference import UPDATED, ADDED, REMOVED


INDENT = '    '
ADDED_FLAG = '+'
REMOVED_FLAG = '-'
UNMODIFIED_FLAG = ' '
UPDATED_FLAG = '-'
STRINGS_OF_TYPES = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def get_stylish(diffs):
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
            result.append(diff_line(cur_indent, type, name, value, new_value))
        result_string = make_result_string('\n'.join(result), cur_indent)
        return result_string
    return walk(diffs)


def diff_line(indent, diff_type, name, value, new_value):
    value = format_value(value, indent)
    new_value = format_value(new_value, indent)
    flag = ''
    if diff_type == ADDED:
        flag = ADDED_FLAG
    elif diff_type == REMOVED:
        flag = REMOVED_FLAG
    elif diff_type == UPDATED:
        flag = UPDATED_FLAG
    else:
        flag = UNMODIFIED_FLAG
    line = format_string(indent, flag, name, value)
    if diff_type is UPDATED:
        updated_line = format_string(indent, ADDED_FLAG, name, new_value)
        line = '\n'.join([line, updated_line])
    return line


def format_value(value, intend):
    if isinstance(value, dict):
        value = get_formatted_dict(value, intend + INDENT)
    elif isinstance(value, bool) or value is None:
        value = STRINGS_OF_TYPES[value]
    return value


def format_string(indent, flag, key, value):
    return '{}  {} {}: {}'.format(indent, flag, key, value)


def get_formatted_dict(items, indent):
    sorted_items = sorted(items.items())
    result = []
    for (key, value) in sorted_items:
        if isinstance(value, dict):
            value = get_formatted_dict(value, indent + INDENT)
        result.append(format_string(indent, ' ', key, value))
    result_string = make_result_string('\n'.join(result), indent)
    return result_string


def make_result_string(result, indent):
    result_string = '{{\n{}\n{}}}'.format(result, indent)
    return result_string
