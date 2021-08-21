from gendiff.scripts.gendiff import generate_diff
from os.path import abspath
import pytest


expected_diff = 'tests/fixtures/test_gendiff/exp_diff'


@pytest.mark.parametrize("file1,file2", [(
    'tests/fixtures/test_gendiff/input_file1.json',
    'tests/fixtures/test_gendiff/input_file2.json'), (
    'tests/fixtures/test_gendiff/input_file1.yaml',
    'tests/fixtures/test_gendiff/input_file2.yml'),
])
def test_generate_diff(file1, file2):
    with open(abspath(expected_diff), 'r') as file:
        data = file.read()
    assert generate_diff(file1, file2) == data
