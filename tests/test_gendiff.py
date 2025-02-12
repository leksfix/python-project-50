
from pathlib import Path

from gendiff.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff_json_stylish():
    assert generate_diff(
        get_test_data_path('file1.json'),
        get_test_data_path('file2.json'),
        'stylish'
    ) == read_file('diff_stylish.txt')


def test_gendiff_yaml_stylish():
    assert generate_diff(
        get_test_data_path('file1.yaml'),
        get_test_data_path('file2.yaml'),
        'stylish'
    ) == read_file('diff_stylish.txt')