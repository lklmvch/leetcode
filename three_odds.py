"""Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false."""


def threeConsecutiveOdds(arr):
    odds = 0
    for i in arr:
        if i % 2 != 0:
            odds += 1
            if odds == 3:
                return True
        else:
            odds = 0
    return False
