import argparse
from gendiff.formatters.formatter import FORMATTERS, STYLISH


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default=STYLISH,
        choices=list(FORMATTERS),
        help='set format of output')
    return parser.parse_args()
