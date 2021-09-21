from json import dumps
from gendiff.difference import get_name
from typing import List, Tuple, Any


def get_json(diffs: List[Tuple[str, str, Any, Any]]) -> str:
    diffs = sorted(diffs, key=get_name)
    return dumps(diffs)
