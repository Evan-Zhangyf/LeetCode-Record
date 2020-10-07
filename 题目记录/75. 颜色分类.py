class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for i in nums:
            cnt[i] += 1
        for i in range(cnt[0]):
            nums[i] = 0
        for i in range(cnt[0], cnt[0] + cnt[1]):
            nums[i] = 1
        for i in range(cnt[0] + cnt[1], cnt[0] + cnt[1] + cnt[2]):
            nums[i] = 2