from typing import Any, List, Tuple


Diff = Tuple[str, str, Any, Any]
ADDED = 'ADDED'
REMOVED = 'REMOVED'
UNMODIFIED = 'UNMODIFIED'
UPDATED = 'UPDATED'
NESTED = 'NESTED'


def get_diff(dict1: dict, dict2: dict) -> List[Diff]:
    added_keys = set(dict2) - set(dict1)
    removed_keys = set(dict1) - set(dict2)
    common_keys = set(dict1) & set(dict2)
    diffs = []
    for key in added_keys:
        diffs.append(make_diff(ADDED, key, dict2[key]))
    for key in removed_keys:
        diffs.append(make_diff(REMOVED, key, dict1[key]))
    for key in common_keys:
        if dict1[key] == dict2[key]:
            diffs.append(make_diff(UNMODIFIED, key, dict1[key]))
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = get_diff(dict1[key], dict2[key])
            diffs.append(make_diff(NESTED, key, nested_diff))
        else:
            diffs.append(make_diff(UPDATED, key, dict1[key], dict2[key]))
    return diffs


def make_diff(flag: str, key: str, value: Any, changed_value=None) -> Diff:
    return (flag, key, value, changed_value)


def get_type(diff: Tuple) -> str:
    return diff[0]


def get_name(diff: Tuple) -> str:
    return diff[1]


def get_value(diff: Tuple) -> Any:
    return diff[2]


def get_new_value(diff: Tuple) -> Any:
    return diff[3]


def has_children(diff: Tuple) -> bool:
    if diff[0] is NESTED:
        return True
    return False
