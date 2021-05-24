class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先搜索旋转点（最小值的索引）
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[-1]:
                r = m
            else:
                l = m + 1
        idx = l
        # 分别在[0, idx]和[idx, len(nums) - 1]中搜索target（这里不在[idx + 1, len(nums) - 1]中搜索是为了防止处理数组的边界条件）
        l = 0
        r = idx
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] == target:
            return l
        
        l = idx
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] == target:
            return l
        return -1