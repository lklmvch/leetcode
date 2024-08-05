"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""


from collections import Counter
def uniqueOccurrences(arr):
    cnt = Counter(arr)
    lst = [v for v in cnt.values()]
    return len(lst) == len(set(lst))

