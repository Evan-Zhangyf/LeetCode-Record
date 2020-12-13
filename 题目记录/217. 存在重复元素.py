class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if not dic.get(i):
                dic[i] = True
            else:
                return True
        return False