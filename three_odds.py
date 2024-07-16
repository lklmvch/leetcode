"""Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false."""

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        odds = 0
        for i in arr:
            if i % 2 != 0:
                odds += 1
                if odds == 3:
                    return True
            else:
                odds = 0
        return False
