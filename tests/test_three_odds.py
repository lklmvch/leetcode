from three_odds import threeConsecutiveOdds
import pytest


@pytest.mark.parametrize('arr, expected_result', [([2,6,4,1], False), ([1, 2, 34, 3, 4, 5, 7, 23, 12], True)])
def test_threeConsecutiveOdds(arr, expected_result):
    assert threeConsecutiveOdds(arr) == expected_result
