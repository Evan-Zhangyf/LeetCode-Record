class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        ans = s[0]
        dp = [[True] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1 , -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    max_len = max(max_len, j - i + 1)
                    if j - i + 1 == max_len:
                        ans = s[i: j+1]
        return ans