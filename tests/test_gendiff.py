
from pathlib import Path

import pytest

from gendiff.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


@pytest.mark.parametrize("filename1, filename2, format, res_filename", [
    ('file1.json', 'file2.json', 'stylish', 'diff_stylish.txt'),
    ('file1.yaml', 'file2.yaml', 'stylish', 'diff_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'diff_plain.txt'),
    ('file1.yaml', 'file2.yaml', 'plain', 'diff_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'diff_json.txt'),
    ('file1.yaml', 'file2.yaml', 'json', 'diff_json.txt')
])
def test_gendiff_result(filename1, filename2, format, res_filename):
    assert generate_diff(
        get_test_data_path(filename1),
        get_test_data_path(filename2),
        format
    ) == read_file(res_filename)


def test_unknown_format():
    with pytest.raises(ValueError, match="Unknown format: 'wrong'"):
        generate_diff(
            get_test_data_path('file1.json'),
            get_test_data_path('file2.json'),
            'wrong'
        )


def test_unknown_file_type():
    with pytest.raises(ValueError, match="Unknown file type: 'bad'"):
        generate_diff(
            get_test_data_path('file1.bad'),
            get_test_data_path('file2.bad'),
            'stylish'
        )
