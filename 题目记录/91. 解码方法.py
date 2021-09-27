class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
            dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            tmp = int(s[i-2: i])
            if tmp <= 26 and tmp >= 10:
                dp[i] += dp[i-2]
        return dp[-1]