from gendiff.compare import get_diff_list
from gendiff.formatters import get_formatter
from gendiff.parse import parse_file


def generate_diff(filename1, filename2, format='stylish'):
    """Generates diff string using 'format' argument"""
    file1 = parse_file(filename1)
    file2 = parse_file(filename2)
    diff_list = get_diff_list(file1, file2)
    return get_formatter(format)(diff_list)
