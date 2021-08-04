class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            k = i + 1
            for j in range(i + 1, len(nums) - 1):
                while k != len(nums) - 1 and nums[k+1] < nums[i] + nums[j]:
                    k += 1
                ans += max(0, k - j)
        return ans