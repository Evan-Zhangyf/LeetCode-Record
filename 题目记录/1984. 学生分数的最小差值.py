class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_val = float("inf")
        for i in range(len(nums) - k + 1):
            min_val = min(min_val, nums[i+k-1] - nums[i])
        return min_val