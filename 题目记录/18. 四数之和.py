class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        n = len(nums) - 1
                        for m in range(j + 1, len(nums) - 1):
                            if m == j + 1 or nums[m] != nums[m-1]:
                                while(m < n and nums[m] + nums[n] > target - nums[i] - nums[j]):
                                    n -= 1
                                if m == n:
                                    break
                                if nums[m] + nums[n] == target - nums[i] - nums[j]:
                                    ans.append([nums[i], nums[j], nums[m], nums[n]])

        return ans