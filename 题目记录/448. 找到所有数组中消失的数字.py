class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            nums[nums[i] % len(nums) - 1] += len(nums)
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                ans.append(i + 1)
        return ans