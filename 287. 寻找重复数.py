class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if not(i in dict):
                dict[i] = 1
            else:
                dup = i
                break
        return dup