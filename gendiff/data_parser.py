import json
import yaml
from os.path import abspath


def parse_data(filepath):
    data = get_file_data(filepath)
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.load(data, Loader=yaml.Loader)
    elif filepath.endswith('.json'):
        return json.loads(data)
    raise ValueError


def get_file_data(filepath):
    with open(abspath(filepath), 'r') as file:
        data = file.read()
    return data
