from gendiff.parser import get_file
from gendiff.result_maker import get_string_result


def generate_diff(filepath1, filepath2):
    file1 = get_file(filepath1)
    file2 = get_file(filepath2)
    result = get_diff(file1, file2)
    result_string = get_string_result(result)
    return result_string


def get_diff(file1, file2):
    not_in_file1 = set(file2) - set(file1)
    not_in_file2 = set(file1) - set(file2)
    intersection = set(file1) & set(file2)
    result = []
    for key in not_in_file1:
        result.append(make_addition(key, file2[key]))
    for key in not_in_file2:
        result.append(make_remove(key, file1[key]))
    for key in intersection:
        if file1[key] == file2[key]:
            result.append(make_no_change(key, file1[key]))
            continue
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            nested_diff = get_diff(file1[key], file2[key])
            result.append(make_no_change(key, nested_diff, nested_flag=True))
        else:
            result.append(make_changed(key, file1[key], file2[key]))
    return sorted(result, key=lambda key: key[1])


def make_diff(flag, key, value, changed_value=None, nested=False):
    if isinstance(value, dict):
        nested = True
    return (flag, key, value, changed_value, nested)


def make_addition(key, value):
    diff = make_diff('+', key, value)
    return diff


def make_remove(key, value):
    diff = make_diff('-', key, value)
    return diff


def make_no_change(key, value, nested_flag=False):
    diff = make_diff(' ', key, value, nested=nested_flag)
    return diff


def make_changed(key, initial_value, changed_value):
    diff = make_diff('-+', key, initial_value, changed_value)
    return diff


def change_value(diff, new_value):
    diff = make_diff(get_flag(diff), get_name(diff), new_value)
    return diff


def get_flag(diff):
    return diff[0]


def get_name(diff):
    return diff[1]


def get_value(diff):
    value = diff[2]
    if isinstance(value, dict):
        return get_diff(value, value)
    return value


def get_changed_value(diff):
    return diff[3]


def is_removed(diff):
    if diff[0] == '-':
        return True
    return False


def is_added(diff):
    if diff[0] == '+':
        return True
    return False


def is_not_changed(diff):
    if diff[0] == ' ':
        return True
    return False


def is_changed(diff):
    if diff[0] == '-+':
        return True
    return False


def has_children(diff):
    return diff[4]
