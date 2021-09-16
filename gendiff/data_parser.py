import json
import yaml
from os.path import abspath, splitext


LOADERS = {
    '.yaml': yaml.load,
    '.yml': yaml.load,
    '.json': json.loads
}


def get_data(filepath):
    extension = splitext(filepath)[1]
    load = get_data_loader(extension)
    if load:
        data = get_file_data(filepath)
        return load(data)
    raise ValueError


def get_data_loader(extension):
    extension = extension.lower()
    if extension in LOADERS:
        return LOADERS[extension]
    return None


def get_file_data(filepath):
    with open(abspath(filepath), 'r') as file:
        data = file.read()
    return data
