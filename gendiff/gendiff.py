from gendiff.compare import get_diffs
from gendiff.formatters import get_formatter
from gendiff.parse import parse_file


def generate_diff(filename1, filename2, format='stylish'):
    """Generates diff string using 'format' argument"""
    file1 = parse_file(filename1)
    file2 = parse_file(filename2)
    diffs = get_diffs(file1, file2)
    return get_formatter(format)(diffs)
