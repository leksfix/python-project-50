from gendiff.compare import get_diff_list
from gendiff.diff_format import format_stylish
from gendiff.parse import parse_json, parse_yaml


def generate_diff(filename1, filename2, format='stylish'):
    """Generates diff string using 'format' argument"""
    ext1 = str(filename1).split('.')[-1].lower()
    ext2 = str(filename2).split('.')[-1].lower()
    if ext1 != ext2:
        return 'Different file types'
    if ext1 == 'json':
        file1 = parse_json(filename1)
        file2 = parse_json(filename2)
    elif ext1 in {'yml', 'yaml'}:
        file1 = parse_yaml(filename1)
        file2 = parse_yaml(filename2)
    else:
        return 'Unknown file type'
        
    diff_list = get_diff_list(file1, file2)
    match format:
        case 'stylish':
            return format_stylish(diff_list)
        case _:
            return 'Unknown format'
    
