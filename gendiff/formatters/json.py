from json import dumps
from gendiff.difference import get_name

def get_json(diffs):
    diffs = sorted(diffs, key = get_name)
    return dumps(diffs)
