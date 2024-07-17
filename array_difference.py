"""Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1."""


def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    result = [[], []]
    for i in nums1:
        if i not in nums2 and i not in result[0]:
            result[0].append(i)

    for i in nums2:
        if i not in nums1 and i not in result[1]:
            result[1].append(i)

    return result
