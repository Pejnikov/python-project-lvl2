from gendiff.scripts.gendiff import generate_diff
from os.path import abspath


def test_generate_diff():
    with open(abspath('tests/fixtures/test_gendiff/expected_diff'), 'r') as file:
        data = file.read()
    assert generate_diff(
        'tests/fixtures/test_gendiff/input_file1.json', 
        'tests/fixtures/test_gendiff/input_file2.json') == data
