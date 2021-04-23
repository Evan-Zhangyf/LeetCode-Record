class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_val = dp[0]
        idx = 0
        for i in range(len(dp)):
            if dp[i] > max_val:
                max_val = dp[i]
                idx = i
        
        subset = []
        while dp[idx] != 1:
            subset.append(nums[idx])
            max_val -= 1
            for i in range(idx - 1, -1, -1):
                if dp[i] == max_val and nums[idx] % nums[i] == 0:
                    idx = i
        subset.append(nums[idx])
        return subset