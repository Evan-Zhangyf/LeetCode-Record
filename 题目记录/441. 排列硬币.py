class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            m = (l + r + 1) // 2
            if (1 + m) * m // 2 > n:
                r = m - 1
            else:
                l = m
        return l