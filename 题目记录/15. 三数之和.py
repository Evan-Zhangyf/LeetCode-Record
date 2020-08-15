class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i-1]:
                k = len(nums) - 1
                for j in range(i + 1, len(nums) - 1):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        while(j < k and nums[j] + nums[k] > -nums[i]):
                            k -= 1
                        if j == k:
                            break
                        if nums[j] + nums[k] == -nums[i]:
                            ans.append([nums[i], nums[j], nums[k]])
        return ans