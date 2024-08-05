'''Given an integer array sorted in non-decreasing order, there is exactly one integer in the array
that occurs more than 25% of the time, return that integer.'''

def findSpecialInteger(arr):
    percent = len(arr) / 4
    for i in arr:
        if arr.count(i) > percent:
            return i
