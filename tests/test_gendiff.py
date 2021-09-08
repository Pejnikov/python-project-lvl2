from gendiff.diff_engine import generate_diff
from os.path import abspath
import pytest


ARTIFACTS_PATH = 'tests/fixtures/test_gendiff/'


@pytest.mark.parametrize("file1,file2,expected_output", [(
    'hx_plain1.json', 'hx_plain2.json', 'hx_plain_exp',), (
    'hx_plain1.yaml', 'hx_plain2.yml', 'hx_plain_exp',), (
    'deb_rec1.json', 'deb_rec2.json', 'deb_rec_exp',), (
    'hx_rec1.json', 'hx_rec2.json', 'hx_rec_exp',), (
    'hx_rec1.yml', 'hx_rec2.yml', 'hx_rec_exp',
)]
)
def test_stylish_diff(file1, file2, expected_output):
    file1 = make_artifacts_path(file1)
    file2 = make_artifacts_path(file2)
    expected_output = make_artifacts_path(expected_output)
    with open(abspath(expected_output), 'r') as file:
        data = file.read()
    assert generate_diff(file1, file2, 'stylish') == data


@pytest.mark.parametrize("file1,file2,expected_output", [(
    'hx_plain1.json', 'hx_plain2.json', 'hx_plain_fplain_exp',), (
    'deb_rec1.json', 'deb_rec2.json', 'deb_rec_fplain_exp',), (
    'hx_rec1.json', 'hx_rec2.json', 'hx_rec_fplain_exp',
)]
)
def test_plain_diff(file1, file2, expected_output):
    file1 = make_artifacts_path(file1)
    file2 = make_artifacts_path(file2)
    expected_output = make_artifacts_path(expected_output)
    with open(abspath(expected_output), 'r') as file:
        data = file.read()
    assert generate_diff(file1, file2, 'plain') == data


@pytest.mark.parametrize("file1,file2,expected_output", [(
    'deb_rec1.json', 'deb_rec2.json', 'deb_rec_fjson_exp',
)]
)
def test_json_diff(file1, file2, expected_output):
    file1 = make_artifacts_path(file1)
    file2 = make_artifacts_path(file2)
    expected_output = make_artifacts_path(expected_output)
    with open(abspath(expected_output), 'r') as file:
        data = file.read()
    assert generate_diff(file1, file2, 'json') == data


def make_artifacts_path(file):
    return ARTIFACTS_PATH + file


def test_invalid_input():
    fake_data = make_artifacts_path('fake_data.jpeg')
    with pytest.raises(ValueError):
        generate_diff(fake_data, fake_data)