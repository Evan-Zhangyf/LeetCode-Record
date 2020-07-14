class Solution:
    def numTrees(self, n: int) -> int:
        # 特判
        if n == 1 or n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]