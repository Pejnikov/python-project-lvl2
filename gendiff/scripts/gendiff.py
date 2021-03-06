from gendiff.diff_engine import generate_diff
from gendiff.args_parser import get_args


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
