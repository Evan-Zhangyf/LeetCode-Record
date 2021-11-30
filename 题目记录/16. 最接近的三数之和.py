class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < abs(ans - target):
                    ans = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    return target
        return ans