class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        dp_min = [0] * len(nums)
        dp_min[-1] = nums[-1]
        for i in range(len(dp_min) - 2, -1, -1):
            dp_min[i] = min(dp_min[i+1], nums[i])
        cur_max = nums[0]
        for i in range(0, len(nums) - 1):
            cur_max = max(cur_max, nums[i])
            if cur_max <= dp_min[i+1]:
                ans = i + 1
                break
        return ans