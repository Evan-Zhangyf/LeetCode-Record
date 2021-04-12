class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def switch(x, y):
            if x + y > y + x:
                return False
            else:
                return True

        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if switch(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        ans = "".join(nums)
        if len(ans) > 1 and ans[0] == "0":
            return "0"
        else:
            return ans