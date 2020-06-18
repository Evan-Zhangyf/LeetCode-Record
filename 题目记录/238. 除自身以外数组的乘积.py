class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
            right_product[len(nums)-1-i] = right_product[len(nums)-i] * nums[len(nums)-i]
        return [left_product[i]*right_product[i] for i in range(len(nums))]