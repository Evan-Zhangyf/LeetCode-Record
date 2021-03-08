class Solution:
    def minCut(self, s: str) -> int:
        is_palindrome = [[True] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i + 1][j - 1]
        dp = [0] * len(s)
        for i in range(1, len(s)):
            tmp = len(s)
            for j in range(0, i + 1):
                if is_palindrome[j][i]:
                    if j == 0:
                        tmp = 0
                    else:
                        tmp = min(tmp, dp[j-1] + 1)
            dp[i] = tmp
        return dp[-1]