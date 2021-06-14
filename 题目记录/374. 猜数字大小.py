# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        from math import ceil
        l = 1
        r = n
        while l < r:
            m = ceil((l + r) / 2)
            if guess(m) == -1:
                r = m - 1
            else:
                l = m
        return l