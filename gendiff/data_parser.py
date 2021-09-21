import json
import yaml
from os.path import abspath, splitext
from typing import Optional, Callable, Dict


LOADERS: Dict[str, Callable] = {
    '.yaml': yaml.load,
    '.yml': yaml.load,
    '.json': json.loads
}


def get_data(filepath: str) -> dict:
    extension = splitext(filepath)[1]
    load = get_data_loader(extension)
    if load:
        data = get_file_data(filepath)
        return load(data)
    raise ValueError


def get_data_loader(extension: str) -> Optional[Callable]:
    extension = extension.lower()
    if extension in LOADERS:
        return LOADERS[extension]
    return None


def get_file_data(filepath: str) -> str:
    with open(abspath(filepath), 'r') as file:
        data = file.read()
    return data
