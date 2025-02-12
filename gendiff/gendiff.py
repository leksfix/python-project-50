from gendiff.compare import get_diff
from gendiff.diff_format import format_stylish
from gendiff.parse import parse_json


def generate_diff(filename1, filename2, format='stylish'):
    """Generates diff string using 'format' argument"""
    file1 = parse_json(filename1)
    file2 = parse_json(filename2)
    diff = get_diff(file1, file2)
    match format:
        case 'stylish':
            return format_stylish(diff)
        case _:
            return format_stylish(diff)

    
