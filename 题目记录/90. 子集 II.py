class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def back(state, pos):
            ans.append(state)
            if pos == len(nums) - 1:
                return
            pre = nums[pos + 1] - 1
            for i in range(pos + 1, len(nums)):
                if pre != nums[i]:
                    back(state + [nums[i]], i)
                pre = nums[i]
        back([], -1)
        return ans
