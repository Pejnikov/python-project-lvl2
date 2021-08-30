from gendiff.diff_engine import generate_diff
from os.path import abspath
import pytest


#hx_plain_exp = hx_plain_exp'
#rec_exp_diff = 'tests/fixtures/test_gendiff/hx_rec_exp'

artifacts_path = 'tests/fixtures/test_gendiff/'

@pytest.mark.parametrize("file1,file2,expected_diff", [(
    'hx_plain1.json', 'hx_plain2.json', 'hx_plain_exp',), (
    'hx_plain1.yaml', 'hx_plain2.yml', 'hx_plain_exp',), (
    'deb_rec1.json', 'deb_rec2.json', 'deb_rec_exp',), (
    'hx_rec1.json', 'hx_rec2.json', 'hx_rec_exp',), (
    'hx_rec1.yml', 'hx_rec2.yml', 'hx_rec_exp',
    )
])
def test_generate_diff(file1, file2, expected_diff):
    file1 = artifacts_path + file1
    file2 = artifacts_path + file2
    expected_diff = artifacts_path + expected_diff
    with open(abspath(expected_diff), 'r') as file:
        data = file.read()
    print(generate_diff(file1, file2))
    print(data)
    assert generate_diff(file1, file2) == data
