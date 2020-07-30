class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = max([max(dp[i - j], i - j) * j for j in range(1, i)])
        return dp[-1]