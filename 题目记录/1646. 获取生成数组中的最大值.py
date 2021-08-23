class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [0, 1]
        ans = 1
        for i in range(2, n + 1):
            if i % 2 == 1:
                tmp = nums[i//2] + nums[i//2+1]
            else:
                tmp = nums[i//2]
            nums.append(tmp)
            ans = max(tmp, ans)
        return ans