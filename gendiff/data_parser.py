import json
import yaml
from os.path import abspath, basename
from fnmatch import fnmatch


LOADERS = {
    ('*?.yaml', yaml.load),
    ('*?.yml', yaml.load),
    ('*?.json', json.loads),
}


def get_data(filepath):
    filename = basename(filepath)
    load = get_data_loader(filename)
    if load:
        data = get_file_data(filepath)
        return load(data)
    raise ValueError


def get_data_loader(filename):
    filename = filename.lower()
    for (search_pattern, loader) in LOADERS:
        if fnmatch(filename, search_pattern):
            return loader
    return None


def get_file_data(filepath):
    with open(abspath(filepath), 'r') as file:
        data = file.read()
    return data
