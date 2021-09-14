from gendiff.difference import get_name, get_value, get_type, get_new_value
from gendiff.difference import DIFF_TYPES, has_children
from gendiff.formatters.common import get_type_string, need_string

PATH_DIVIDER = '.'


def get_plain(diffs):
    def walk(diffs, name):
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
            if diff_type is DIFF_TYPES['UNMODIFIED']:
                continue
            main_string = plain_string(diff_type, cur_name, value, new_value)
            result.append(main_string)
        return '\n'.join(result)
    return walk(diffs, name='')


def plain_string(diff_type, name, value, new_value):
    result = ''
    first_msg_part = "Property '{}' was ".format(name)
    second_msg_part = make_diff_msg(diff_type, value, new_value)
    result = "{}{}".format(first_msg_part, second_msg_part)
    return result


def make_diff_msg(diff_type, value, new_value=None):
    diff_msg = ''
    value = format_value(value)
    new_value = format_value(new_value)
    if diff_type is DIFF_TYPES['ADDED']:
        diff_msg += "added with value: {}".format(value)
    elif diff_type is DIFF_TYPES['REMOVED']:
        diff_msg += "removed"
    elif diff_type is DIFF_TYPES['UPDATED']:
        diff_msg += "updated. From {} to {}".format(value, new_value)
    return diff_msg


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif need_string(value):
        return get_type_string(value)
    elif isinstance(value, int):
        return value
    value = "'{}'".format(value)
    return value
