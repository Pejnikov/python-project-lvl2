import argparse
import json
import yaml
from os.path import abspath


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def get_file(filepath):
    filepath = abspath(filepath)
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.load(open(filepath), Loader=yaml.Loader)
    return json.load(open(filepath))
