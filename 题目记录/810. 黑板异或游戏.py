class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        tmp = 0
        for i in nums:
            tmp = tmp ^ i
        if tmp == 0 or len(nums) % 2 == 0:
            return True
        else:
            return False