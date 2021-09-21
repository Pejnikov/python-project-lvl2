from json import dumps
from gendiff.difference import get_name, Diff
from typing import List


def get_json(diffs: List[Diff]) -> str:
    diffs = sorted(diffs, key=get_name)
    return dumps(diffs)
