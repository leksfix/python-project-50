from formats import format_plain, format_stylish
from gendiff.compare import get_diff_list
from gendiff.parse import parse_file


def generate_diff(filename1, filename2, format='stylish'):
    """Generates diff string using 'format' argument"""
    file1 = parse_file(filename1)
    file2 = parse_file(filename2)
    if file1 is None or file2 is None:
        return 'Bad file'
    diff_list = get_diff_list(file1, file2)
    match format:
        case 'stylish':
            return format_stylish(diff_list)
        case 'plain':
            return format_plain(diff_list)
        case _:
            return 'Unknown format'
    
