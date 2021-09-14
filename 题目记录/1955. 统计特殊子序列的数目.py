class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = pow(10, 9) + 7
        dp = [[0] * 3 for _ in range(len(nums))]
        if nums[0] == 0:
            dp[0][0] = 1
        for i in range(1, len(nums)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]
            dp[i][2] = dp[i-1][2]
            if nums[i] == 0:
                dp[i][0] = (2 * dp[i-1][0] + 1) % mod
            elif nums[i] == 1:
                dp[i][1] = (dp[i-1][0] + 2 * dp[i][1]) % mod
            else:
                dp[i][2] = (dp[i-1][1] + 2 * dp[i][2]) % mod
        return dp[len(nums)-1][2]
