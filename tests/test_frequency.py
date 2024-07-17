import pytest

from frequency import findSpecialInteger


@pytest.mark.parametrize('arr, expected_result', [([1,2,2,6,6,6,6,7,10], 6),
                                                  ([1,1], 1)])
def test_findSpecialInteger(arr, expected_result):
    assert findSpecialInteger(arr) == expected_result
