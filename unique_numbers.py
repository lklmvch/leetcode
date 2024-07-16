"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""


from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = Counter(arr)
        lst = [v for v in cnt.values()]
        return len(lst) == len(set(lst))

