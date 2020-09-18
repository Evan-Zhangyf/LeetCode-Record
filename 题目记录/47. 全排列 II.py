class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        from collections import defaultdict
        used_dict = defaultdict(int)
        for i in nums:
            used_dict[i] += 1
        def back(num_list):
            nonlocal used_dict
            if len(num_list) == len(nums):
                ans.append(num_list[:])
                return
            cur_used = {}
            for i in range(len(nums)):
                if not cur_used.get(nums[i]) and used_dict[nums[i]] > 0:
                    used_dict[nums[i]] -= 1
                    cur_used[nums[i]] = True
                    num_list.append(nums[i])
                    back(num_list)
                    used_dict[nums[i]] += 1 
                    num_list.pop()

        back([])
        return ans