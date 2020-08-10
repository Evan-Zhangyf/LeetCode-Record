class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # dp中记录包括自己在内，之前连续等于自己的字符串长度
        dp = [1] * len(s)
        ans = 0
        for i in range(1, len(s)):
            cur = s[i]
            if s[i-1] != cur:
                ans += 1
            else:
                dp[i] = dp[i-1] + 1
                if dp[i-1] == i:
                    continue
                else:
                    if dp[i - dp[i]] >= dp[i]:
                        ans += 1
        return ans