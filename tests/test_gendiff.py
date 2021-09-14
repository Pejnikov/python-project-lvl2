from gendiff.diff_engine import generate_diff
from os.path import abspath
import pytest


@pytest.mark.parametrize("format,file1,file2,expected_output", [(
    'stylish',
    'tests/fixtures/test_gendiff/plain/hx_file1.json',
    'tests/fixtures/test_gendiff/plain/hx_file2.json',
    'tests/fixtures/test_gendiff/plain/hx_stylish_exp',
), (
    'plain',
    'tests/fixtures/test_gendiff/plain/hx_file1.json',
    'tests/fixtures/test_gendiff/plain/hx_file2.json',
    'tests/fixtures/test_gendiff/plain/hx_plain_exp',
), (
    'stylish',
    'tests/fixtures/test_gendiff/plain/hx_file1.yaml',
    'tests/fixtures/test_gendiff/plain/hx_file2.yml',
    'tests/fixtures/test_gendiff/plain/hx_stylish_exp',
), (
    'plain',
    'tests/fixtures/test_gendiff/plain/hx_file1.yaml',
    'tests/fixtures/test_gendiff/plain/hx_file2.yml',
    'tests/fixtures/test_gendiff/plain/hx_plain_exp',
), (
    'stylish',
    'tests/fixtures/test_gendiff/recursive/hx_file1.json',
    'tests/fixtures/test_gendiff/recursive/hx_file2.json',
    'tests/fixtures/test_gendiff/recursive/hx_stylish_exp',
), (
    'plain',
    'tests/fixtures/test_gendiff/recursive/hx_file1.json',
    'tests/fixtures/test_gendiff/recursive/hx_file2.json',
    'tests/fixtures/test_gendiff/recursive/hx_plain_exp',
), (
    'stylish',
    'tests/fixtures/test_gendiff/recursive/hx_file1.yml',
    'tests/fixtures/test_gendiff/recursive/hx_file2.yml',
    'tests/fixtures/test_gendiff/recursive/hx_stylish_exp',
), (
    'plain',
    'tests/fixtures/test_gendiff/recursive/hx_file1.yml',
    'tests/fixtures/test_gendiff/recursive/hx_file2.yml',
    'tests/fixtures/test_gendiff/recursive/hx_plain_exp',
), (
    'stylish',
    'tests/fixtures/test_gendiff/recursive/deb_file1.json',
    'tests/fixtures/test_gendiff/recursive/deb_file2.json',
    'tests/fixtures/test_gendiff/recursive/deb_stylish_exp',
), (
    'plain',
    'tests/fixtures/test_gendiff/recursive/deb_file1.json',
    'tests/fixtures/test_gendiff/recursive/deb_file2.json',
    'tests/fixtures/test_gendiff/recursive/deb_plain_exp',
), (
    'json',
    'tests/fixtures/test_gendiff/recursive/deb_file1.json',
    'tests/fixtures/test_gendiff/recursive/deb_file2.json',
    'tests/fixtures/test_gendiff/recursive/deb_json_exp',
),
]
)
def test_diff(file1, file2, expected_output, format):
    with open(abspath(expected_output), 'r') as file:
        data = file.read()
    print(f'>{generate_diff(file1, file2, format)}<')
    print(f'\n>{data}<')
    assert generate_diff(file1, file2, format) == data


def test_wrong_extension():
    fake_data = 'fake_data.jpeg'
    with pytest.raises(ValueError):
        generate_diff(fake_data, fake_data)
