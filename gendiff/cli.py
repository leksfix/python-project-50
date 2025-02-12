""" gendiff CLI"""

import argparse

from gendiff.gendiff import generate_diff


def cli_run():
    """Runs the CLI application"""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        epilog=''
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')

    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))