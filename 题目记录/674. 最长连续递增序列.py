class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        ans = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        return max(ans, cur)