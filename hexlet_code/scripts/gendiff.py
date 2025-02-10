""" gendiff application script"""
import argparse
from hexlet_code.gendiff import generate_diff


def main():
    """Runs the CLI application"""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        epilog=''
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()

    print(generate_diff(args.format, args.first_file, args.second_file))




if __name__ == "__main__":
    main()
