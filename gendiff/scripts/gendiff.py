import argparse
import json
from string import Template


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


def get_string_result(items):
    result = '{\n'
    temp = Template('  $flag $key: $value\n')
    for item in items:
        result += temp.substitute(flag=item[0], key=item[1], value=item[2])
    result += '}'
    return result


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def get_file(filepath):
    return json.load(open(filepath))


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
