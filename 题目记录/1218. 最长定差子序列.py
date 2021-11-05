class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        ret = 1
        for i in arr:
            dp[i] = max(dp[i], dp[i-difference] + 1)
            ret = max(ret, dp[i])
        return ret