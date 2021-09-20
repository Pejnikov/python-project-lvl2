

ADDED = 'ADDED'
REMOVED = 'REMOVED'
UNMODIFIED = 'UNMODIFIED'
UPDATED = 'UPDATED'
NESTED = 'NESTED'


def get_diff(dict1, dict2):
    added_keys = set(dict2) - set(dict1)
    removed_keys = set(dict1) - set(dict2)
    common_keys = set(dict1) & set(dict2)
    diffs = []
    for key in added_keys:
        diffs.append(make_added(key, dict2[key]))
    for key in removed_keys:
        diffs.append(make_removed(key, dict1[key]))
    for key in common_keys:
        if dict1[key] == dict2[key]:
            diffs.append(make_unmodified(key, dict1[key]))
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = get_diff(dict1[key], dict2[key])
            diffs.append(make_nested(key, nested_diff))
        else:
            diffs.append(make_updated(key, dict1[key], dict2[key]))
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
    diff = make_diff(UPDATED, key, initial_value, new_value)
    return diff


def make_nested(key, value):
    diff = make_diff(NESTED, key, value)
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
    if diff[0] is NESTED:
        return True
    return False
