class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        def back(num_list):
            nonlocal used
            if len(num_list) == len(nums):
                ans.append(num_list[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    num_list.append(nums[i])
                    back(num_list)
                    used[i] = False
                    num_list.pop()

        back([])
        return ans