from string import Template
from gendiff import diff_engine


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
            key = diff_engine.get_name(diff)
            value = diff_engine.get_value(diff)
            if diff_engine.has_children(diff):
                value = walk(value, intend + '    ')
            value = to_json(value)
            if diff_engine.is_added(diff):
                result += temp.substitute(flag='+', key=key, value=value)
            elif diff_engine.is_removed(diff):
                result += temp.substitute(flag='-', key=key, value=value)
            elif diff_engine.is_not_changed(diff):
                result += temp.substitute(flag=' ', key=key, value=value)
            else:
                changed_value = diff_engine.get_changed_value(diff)
                changed_value = to_json(changed_value)
                result += temp.substitute(flag='-', key=key, value=value)
                result += temp.substitute(flag='+', key=key, value=changed_value)
        result = '{{\n{}{}}}'.format(result, intend)
        return result
    return walk(diffs)
