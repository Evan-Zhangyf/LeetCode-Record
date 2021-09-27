class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
            if s[0] == '*':
                dp[1] = 9
            else:
                dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != '0':
                if s[i-1] == '*':
                    dp[i] += 9 * dp[i-1]
                else:
                    dp[i] += dp[i-1]
            if s[i-2] == '0':
                continue
            if s[i-1] == '*' and s[i-2] == '*':
                dp[i] += 15 * dp[i-2]
            elif s[i-1] == '*' and s[i-2] != '*':
                if s[i-2] == '2':
                    dp[i] += 6 * dp[i-2]
                elif s[i-2] < '2':
                    dp[i] += 9 * dp[i-2]
            elif s[i-1] != '*' and s[i-2] == '*':
                if s[i-1] > '6':
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 2 * dp[i-2]
            else:
                tmp = int(s[i-2:i])
                if tmp <= 26 and tmp >= 10:
                    dp[i] += dp[i-2]
            dp[i] = dp[i] % mod
        return dp[-1]