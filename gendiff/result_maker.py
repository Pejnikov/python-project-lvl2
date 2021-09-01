from string import Template
from gendiff.difference import get_name, get_value, get_diff
from gendiff.difference import has_children, is_added, is_removed, is_not_changed, get_changed_value

INTENT = '    '


def to_json(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value


def get_string_result(diffs):
    def walk(diffs, intend = ''):
        result = ''
        temp = Template(intend + '  $flag $key: $value\n')
        for diff in diffs:
            key = get_name(diff)
            value = get_value(diff)
            changed_value = get_changed_value(diff)
            if isinstance(changed_value, dict):
                changed_value = get_format(changed_value, intend + INTENT)
            if isinstance(value, dict):
                value = get_format(value, intend + INTENT)
            if has_children(diff):
                value = walk(value, intend + '    ')
            value = to_json(value)
            if is_added(diff):
                result += temp.substitute(flag='+', key=key, value=value)
            elif is_removed(diff):
                result += temp.substitute(flag='-', key=key, value=value)
            elif is_not_changed(diff):
                result += temp.substitute(flag=' ', key=key, value=value)
            else:
                changed_value = to_json(changed_value)
                result += temp.substitute(flag='-', key=key, value=value)
                result += temp.substitute(flag='+', key=key, value=changed_value)
        result = '{{\n{}{}}}'.format(result, intend)
        return result
    return walk(diffs)


def get_diff_string(intend, flag, key, value):
    return '{}  {} {}: {}\n'.format(intend, flag, key, value)


def get_format(items, intent):
    sorted_items = sorted(items.items())
    result = ''
    for (key, value) in sorted_items:
        if isinstance(value, dict):
            value = get_format(value, intent + INTENT)
        result += get_diff_string(intent, ' ', key, value)
    result = '{{\n{}{}}}'.format(result, intent)
    return result
        