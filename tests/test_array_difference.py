from array_difference import findDifference
import pytest

@pytest.mark.parametrize('nums1, nums2, expected_result', [([1,2,3], [2,4,6],[[1,3],[4,6]]),
                                                           ([1,2,3,3], [1,1,2,2], [[3],[]]),
                                                           ([-80,-15,-81,-28,-61,63,14,-45,-35,-10], [-1,-40,-44,41,10,-43,69,10,2], [[-80,-15,-81,-28,-61,63,14,-45,-35,-10],[-1,-40,-44,41,10,-43,69,2]])])
def test_findDifference(nums1, nums2, expected_result):
    assert findDifference(nums1, nums2) == expected_result
