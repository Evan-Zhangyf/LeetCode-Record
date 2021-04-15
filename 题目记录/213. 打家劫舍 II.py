class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(nums):
            if nums == []:
                return 0
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return max(nums)
            dp_max = [0]*len(nums)
            dp_max[0] = nums[0]
            dp_max[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp_max[i] = max(dp_max[i-2]+nums[i], dp_max[i-1])
            return max(dp_max)
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(rob_line(nums[0: len(nums) - 1]), rob_line(nums[1: len(nums)]))