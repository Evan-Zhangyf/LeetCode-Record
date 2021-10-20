class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        ans = 0
        for i in nums:
            ans += i - min_val
        return ans