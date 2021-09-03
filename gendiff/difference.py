
DIFF_TYPES = {
    'ADDED': 'ADDED',
    'REMOVED': 'REMOVED',
    'UNMODIFIED': 'UNMODIFIED',
    'UPDATED': 'UPDATED',
}


def get_diff(file1, file2):
    not_in_file1 = set(file2) - set(file1)
    not_in_file2 = set(file1) - set(file2)
    intersection = set(file1) & set(file2)
    result = []
    for key in not_in_file1:
        result.append(make_added(key, file2[key]))
    for key in not_in_file2:
        result.append(make_removed(key, file1[key]))
    for key in intersection:
        if file1[key] == file2[key]:
            result.append(make_unmodified(key, file1[key]))
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            nested_diff = get_diff(file1[key], file2[key])
            result.append(make_unmodified(key, nested_diff, nested_flag=True))
        else:
            result.append(make_updated(key, file1[key], file2[key]))
    return sorted(result, key=lambda key: key[1])


def make_diff(flag, key, value, changed_value=None, nested=False):
    return (flag, key, value, changed_value, nested)


def make_added(key, value):
    diff = make_diff(DIFF_TYPES['ADDED'], key, value)
    return diff


def make_removed(key, value):
    diff = make_diff(DIFF_TYPES['REMOVED'], key, value)
    return diff


def make_unmodified(key, value, nested_flag=False):
    diff = make_diff(DIFF_TYPES['UNMODIFIED'], key, value, nested=nested_flag)
    return diff


def make_updated(key, initial_value, new_value):
    diff = make_diff(DIFF_TYPES['UPDATED'], key, initial_value, new_value)
    return diff


def get_type(diff):
    return diff[0]


def get_name(diff):
    return diff[1]


def get_value(diff):
    return diff[2]


def get_new_value(diff):
    return diff[3]


def has_children(diff):
    return diff[4]
