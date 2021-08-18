import argparse
import json
from string import Template
from os.path import abspath


def generate_diff(filepath1, filepath2):
    file1 = get_file(filepath1)
    file2 = get_file(filepath2)
    result = []
    for item in set(file2) - set(file1):
        result.append(('+', item, file2[item]))
    for item in set(file1) - set(file2):
        result.append(('-', item, file1[item]))
    for item in set(file1) & set(file2):
        if file1[item] == file2[item]:
            result.append((' ', item, file1[item]))
            continue
        result.append(('-', item, file1[item]))
        result.append(('+', item, file2[item]))
    return get_string_result(sorted(result, key=lambda keyq: keyq[1]))


def transform_to_json(value):
    value = str(value)
    if value == 'True':
        value = 'true'
    elif value == 'False':
        value = 'false'
    elif value == 'None':
        value = 'null'
    return value


def get_string_result(items):
    diff = ''
    temp = Template('  $flag $key: $value\n')
    for item in items:
        value = transform_to_json(item[2])
        diff += temp.substitute(flag=item[0], key=item[1], value=value)
    return '{{\n{}}}'.format(diff)


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def get_file(filepath):
    return json.load(open(abspath(filepath)))


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
