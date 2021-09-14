from gendiff.difference import get_name, get_value, get_type, get_new_value
from gendiff.difference import has_children, ADDED, REMOVED, UNMODIFIED
from gendiff.difference import UPDATED

PATH_DIVIDER = '.'
STRINGS_OF_TYPES = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def get_plain(diffs):
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
            main_string = plain_string(diff_type, cur_name, value, new_value)
            result.append(main_string)
        return '\n'.join(result)
    return walk(diffs, name='')


def plain_string(diff_type, name, value, new_value):
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


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool) or value is None:
        return STRINGS_OF_TYPES[value]
    elif isinstance(value, int):
        return value
    value = "'{}'".format(value)
    return value
