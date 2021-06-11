class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            min_num = i
            j = 1
            while j * j <= i:
                min_num = min(min_num, 1 + dp[i - j * j])
                j += 1
            dp[i] = min_num
        return dp[-1]