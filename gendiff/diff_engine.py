from gendiff.parser import get_file
from gendiff.result_maker import get_string_result


def generate_diff(filepath1, filepath2):
    file1 = get_file(filepath1)
    file2 = get_file(filepath2)
    not_in_file1 = set(file2) - set(file1)
    not_in_file2 = set(file1) - set(file2)
    intersection = set(file1) & set(file2)
    result = []
    for item in not_in_file1:
        result.append(('+', item, file2[item]))
    for item in not_in_file2:
        result.append(('-', item, file1[item]))
    for item in intersection:
        if file1[item] == file2[item]:
            result.append((' ', item, file1[item]))
            continue
        result.append(('-', item, file1[item]))
        result.append(('+', item, file2[item]))
    return get_string_result(sorted(result, key=lambda keyq: keyq[1]))
