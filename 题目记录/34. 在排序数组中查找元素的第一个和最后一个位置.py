class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 特判
        if nums == []:
            return [-1, -1]
        # 查找第一个大于等于target的位置
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return [-1, -1]
        ans = [l]
        # 查找最后一个等于target的位置
        r = len(nums) - 1
        from math import ceil
        while l < r:
            m = ceil((l + r) / 2)
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        ans.append(l)
        return ans
