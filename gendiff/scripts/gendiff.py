""" gendiff application script"""

from gendiff.cli import get_args
from gendiff.gendiff import generate_diff_str


def main():
    """Runs the CLI application"""
    args = get_args()
    print(generate_diff_str(*args))


if __name__ == "__main__":
    main()
