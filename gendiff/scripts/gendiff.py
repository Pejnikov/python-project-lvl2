import argparse
import json
from string import Template


def generate_diff(filepath1, filepath2):
    file1 = get_file(filepath1)
    file2 = get_file(filepath2)
    keys = sorted(set(file1) | set(file2))
    result = '{\n'
    temp = Template('  $flag $key $value\n')
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result += temp.substitute(flag=' ', key=key, value=file1[key])
                continue
            result += temp.substitute(flag='-', key=key, value=file1[key])
            result += temp.substitute(flag='+', key=key, value=file2[key])
            continue
        if key in file1:
            result += temp.substitute(flag='-', key=key, value=file1[key])
            continue
        result += temp.substitute(flag='+', key=key, value=file2[key])
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
