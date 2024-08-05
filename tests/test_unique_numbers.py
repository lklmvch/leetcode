from unique_numbers import uniqueOccurrences
import pytest


@pytest.mark.parametrize('arr, expected_result', [([1, 2, 2, 1, 1, 3], True), ([1, 2], False)])
def test_uniqueOccurrences(arr, expected_result):
    assert uniqueOccurrences(arr) == expected_result
