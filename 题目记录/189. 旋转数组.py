class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        for i in range(k // 2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range(((len(nums)) - k) // 2):
            nums[k+i], nums[-i-1] = nums[-i-1], nums[k+i]
        return nums