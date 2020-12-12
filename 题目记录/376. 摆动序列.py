class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pre_up = 1
        pre_down = 1
        for i in range(1, len(nums)):
            # up
            if nums[i] > nums[i-1]:
                pre_up = max(pre_up, pre_down + 1)
            # down
            if nums[i] < nums[i-1]:
                pre_down = max(pre_up + 1, pre_down)
        return max(pre_up, pre_down)