

ADDED = 'ADDED'
REMOVED = 'REMOVED'
UNMODIFIED = 'UNMODIFIED'
UPDATED = 'UPDATED'


def get_diff(file1, file2):
    not_in_file1 = set(file2) - set(file1)
    not_in_file2 = set(file1) - set(file2)
    intersection = set(file1) & set(file2)
    diffs = []
    for key in not_in_file1:
        diffs.append(make_added(key, file2[key]))
    for key in not_in_file2:
        diffs.append(make_removed(key, file1[key]))
    for key in intersection:
        if file1[key] == file2[key]:
            diffs.append(make_unmodified(key, file1[key]))
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            nested_diff = get_diff(file1[key], file2[key])
            diffs.append(make_unmodified(key, nested_diff))
        else:
            diffs.append(make_updated(key, file1[key], file2[key]))
    return diffs


def make_diff(flag, key, value, changed_value=None):
    return (flag, key, value, changed_value)


def make_added(key, value):
    diff = make_diff(ADDED, key, value)
    return diff


def make_removed(key, value):
    diff = make_diff(REMOVED, key, value)
    return diff


def make_unmodified(key, value):
    diff = make_diff(UNMODIFIED, key, value)
    return diff


def make_updated(key, initial_value, new_value):
    diff = make_diff('UPDATED', key, initial_value, new_value)
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
    if diff[0] is UNMODIFIED:
        if isinstance(diff[2], list):
            if isinstance(diff[2][0], tuple):
                return True
    return False
