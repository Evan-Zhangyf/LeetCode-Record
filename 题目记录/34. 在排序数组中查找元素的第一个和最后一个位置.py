class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if ans[0] == -1:
                    ans[0] = i
                    ans[1] = i
                else:
                    ans[1] = i
        return ans