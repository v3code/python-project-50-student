import pytest
from gendiff import generate_diff


file1 = ("tests/fixtures/file1.json")
file2 = ("tests/fixtures/file2.json")
file1yaml = ("tests/fixtures/file1.yml")
file2yaml = ("tests/fixtures/file2.yml")
with open("tests/fixtures/result") as file:
    expected = file.read()


@pytest.mark.parametrize(
    "file_1, file_2",
    [
        (file1, file2),
        (file1yaml, file2yaml),
    ]
)
def test_generate_diff(file_1, file_2):
    assert generate_diff(file_1, file_2) == expected
