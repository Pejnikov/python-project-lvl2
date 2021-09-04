import argparse
import json
import yaml
from os.path import abspath


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', 
        '--format', 
        default='stylish', 
        help='set format of output')
    return parser.parse_args()


def parse_data(filepath):
    data = get_file_data(filepath)
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.load(data, Loader=yaml.Loader)
    return json.loads(data)


def get_file_data(filepath):
    with open(abspath(filepath), 'r') as file:
        data = file.read()
    return data
