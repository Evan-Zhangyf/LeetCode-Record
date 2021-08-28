class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        ans = []
        for i in nums:
            cur += i
            ans.append(cur)
        return ans