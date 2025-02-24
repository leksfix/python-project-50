""" gendiff application script"""

from gendiff.cli import get_args
from gendiff.gendiff import generate_diff


def main():
    """Runs the CLI application"""
    args = get_args()
    print(generate_diff(*args))


if __name__ == "__main__":
    main()
