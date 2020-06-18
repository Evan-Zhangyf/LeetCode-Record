class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        dp = [0]*len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            dp[i] = dp[i-1] + 1
            for j in range(1, dp[i-1]+1):
                if s[i]==s[i-j]:
                    dp[i] = j
        return max(dp)