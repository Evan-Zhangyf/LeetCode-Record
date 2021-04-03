class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    if i == 0:
                        tmp1 = 0
                    else:
                        tmp1 = dp[i-1][j]
                    if j == 0:
                        tmp2 = 0
                    else:
                        tmp2 = dp[i][j-1]
                    dp[i][j] = max(tmp1, tmp2)
        return dp[-1][-1]