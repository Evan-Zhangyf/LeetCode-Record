class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = [-1] * len(s)
        left_dic = {}
        for i in range(len(s)):
            if left_dic.get(s[i]) != None:
                left[i] = left_dic[s[i]]
            left_dic[s[i]] = i
        dp = [1] * len(s)
        ans = 1
        for i in range(1, len(s)):
            if i - left[i] > dp[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = i - left[i]
            ans = max(ans, dp[i])
        return ans