from gendiff.data_parser import parse_data
from gendiff.difference import get_diff
from gendiff.formatters.formatter import get_formater


def generate_diff(filepath1, filepath2, formatter_name='stylish'):
    file1 = parse_data(filepath1)
    file2 = parse_data(filepath2)
    result = get_diff(file1, file2)
    formatter = get_formater(formatter_name)
    formatted_string = formatter(result)
    return formatted_string
