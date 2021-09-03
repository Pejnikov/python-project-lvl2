from gendiff.parser import get_file
from gendiff.formatters.stylish import get_stylish
from gendiff.difference import get_diff


def generate_diff(filepath1, filepath2, formater=get_stylish):
    file1 = get_file(filepath1)
    file2 = get_file(filepath2)
    result = get_diff(file1, file2)
    result_string = formater(result)
    return result_string
