class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        cnt = 0
        dp = [0] * len(nums)
        cnt = [1] * len(nums)
        max_val = 0
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        cnt[i] = cnt[j]
                        dp[i] = dp[j] + 1
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
        dp_max = max(dp)
        ans = 0
        for i in range(len(dp)):
            if dp[i] == dp_max:
                ans += cnt[i]
        return ans