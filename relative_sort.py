"""Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order."""

from collections import Counter
def relativeSortArray(arr1, arr2):
    cnt = Counter(arr1)
    res = []

    for i in arr2:
        if i in cnt.keys():
            for _ in range(cnt[i]):
                res.append(i)
                arr1.remove(i)

    arr1 = sorted(arr1)
    res.extend(arr1)

    return res
