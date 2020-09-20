class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(num_list, last_index):
            ans.append(num_list)
            for i in range(last_index + 1, len(nums)):
                back(num_list + [nums[i]], i)

        back([], -1)
        return ans