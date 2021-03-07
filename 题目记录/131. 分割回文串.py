class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[True] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        ans = []
        def back(state, pos):
            if pos == len(s):
                ans.append(state)
                return
            for i in range(pos, len(s)):
                if dp[pos][i]:
                    back(state + [s[pos:i+1]], i + 1)
        back([], 0)
        return ans