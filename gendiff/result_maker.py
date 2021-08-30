from string import Template
from gendiff.difference import get_name, get_value
from gendiff.difference import has_children, is_added, is_removed, is_not_changed, get_changed_value


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
                changed_value = get_changed_value(diff)
                changed_value = to_json(changed_value)
                result += temp.substitute(flag='-', key=key, value=value)
                result += temp.substitute(flag='+', key=key, value=changed_value)
        result = '{{\n{}{}}}'.format(result, intend)
        return result
    return walk(diffs)
