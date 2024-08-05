from min_num_game import numberGame
import pytest


@pytest.mark.parametrize('nums, expected_result', [([5, 4, 2, 3], [3, 2, 5, 4]), ([2, 5], [5, 2])])
def test_numberGame(nums, expected_result):
    assert numberGame(nums) == expected_result
