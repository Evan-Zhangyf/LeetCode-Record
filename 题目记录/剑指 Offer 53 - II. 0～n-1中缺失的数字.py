class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 特判
        if nums[0] == 1:
            return 0
        if nums[-1] == len(nums) - 1:
            return nums[-1] + 1

        left = 0
        right = len(nums) - 1
        while right - left >= 2:
            mid = int((left + right) / 2)
            if mid - left != nums[mid] - nums[left]:
                right = mid
            else:
                left = mid
        return nums[left] + 1