class Solution:
    def mySqrt(self, x: int) -> int:
        from math import ceil
        l = 0
        r = x
        while l < r:
            m = ceil((l + r) / 2)
            if m * m > x:
                r = m - 1
            else:
                l = m
        return l