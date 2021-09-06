class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        for i in nums:
            right += i
        right -= nums[0]
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
        return -1