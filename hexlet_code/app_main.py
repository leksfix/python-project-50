import argparse


def run_app():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        epilog=''
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    print(args.first_file, args.second_file)
