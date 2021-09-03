from gendiff.parser import parse_data
from gendiff.formatters.stylish import get_stylish
from gendiff.difference import get_diff


def generate_diff(filepath1, filepath2, formater=get_stylish):
    file1 = parse_data(filepath1)
    file2 = parse_data(filepath2)
    result = get_diff(file1, file2)
    result_string = formater(result)
    return result_string
