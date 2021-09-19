class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i-1] = min(dp[i-1], ((i - j) // j) + dp[j-1] + 1)
        return dp[-1]