from gendiff.data_parser import get_data
from gendiff.difference import get_diff
from gendiff.formatters.formatter import get_formater, STYLISH


def generate_diff(filepath1, filepath2, formatter_name=STYLISH):
    file1 = get_data(filepath1)
    file2 = get_data(filepath2)
    result = get_diff(file1, file2)
    formatter = get_formater(formatter_name)
    formatted_string = formatter(result)
    return formatted_string
