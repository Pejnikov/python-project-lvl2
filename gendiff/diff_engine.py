from gendiff.data_parser import get_data
from gendiff.difference import get_diff
from gendiff.formatters.formatter import get_formater, STYLISH


def generate_diff(
    filepath1: str,
    filepath2: str,
    formatter_name: str = STYLISH
) -> str:
    file1 = get_data(filepath1)
    file2 = get_data(filepath2)
    difference = get_diff(file1, file2)
    formatter = get_formater(formatter_name)
    formatted_difference = formatter(difference)
    return formatted_difference
