class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        origin_sum = 0
        nums = nums1[:]
        nums.sort()
        for i in range(len(nums1)):
            origin_sum += abs(nums1[i] - nums2[i])
        ans = origin_sum
        for i in range(len(nums1)):
            tmp = origin_sum - abs(nums1[i] - nums2[i])
            # binary search
            l = 0
            r = len(nums) - 1
            from math import ceil
            while l < r:
                m = ceil((l + r) / 2)
                if nums[m] > nums2[i]:
                    r = m - 1
                else:
                    l = m
            if l < len(nums) - 1:
                tmp = min(tmp + abs(nums[l] - nums2[i]), tmp + abs(nums[l + 1] - nums2[i]))
            else:
                tmp = tmp + abs(nums[l] - nums2[i])
            ans = min(ans, tmp)
        return ans % (10 ** 9 + 7)