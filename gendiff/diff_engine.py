from gendiff.parser import get_file
from gendiff.result_maker import get_string_result
from gendiff.difference import get_diff 


def generate_diff(filepath1, filepath2):
    file1 = get_file(filepath1)
    file2 = get_file(filepath2)
    result = get_diff(file1, file2)
    result_string = get_string_result(result)
    return result_string
