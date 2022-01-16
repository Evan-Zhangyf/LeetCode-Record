class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1, 1, 1, 1, 1]
        for i in range(n - 1):
            tmp1 = dp[1] % mod
            tmp2 = (dp[0] + dp[2]) % mod
            tmp3 = (dp[0] + dp[1] + dp[3] + dp[4]) % mod
            tmp4 = (dp[2] + dp[4]) % mod
            tmp5 = dp[0] % mod
            dp = [tmp1, tmp2, tmp3, tmp4, tmp5]
        return sum(dp) % mod