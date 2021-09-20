class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        max_val = [0] * len(nums)
        min_val = [0] * len(nums)
        max_val[1] = nums[0]
        min_val[-2] = nums[-1]
        for i in range(2, len(nums)):
            max_val[i] = max(max_val[i-1], nums[i-1])
        for i in range(len(nums) - 3, -1, -1):
            min_val[i] = min(min_val[i+1], nums[i+1])
        
        ans = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > max_val[i] and nums[i] < min_val[i]:
                ans += 2
            elif nums[i-1] < nums[i] and nums[i] < nums[i+1]:
                ans += 1
        return ans