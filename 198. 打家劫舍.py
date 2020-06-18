#方法1：dp_max[i]代表以编号i结尾，且打劫编号i的情况下最大金额，复杂度N^2
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dp_max = [0]*len(nums)
        dp_max[0] = nums[0]
        for i in range(1, len(nums)):
            tmp = [a for a in dp_max[:i-1]]
            tmp.append(0)
            dp_max[i] = max(tmp) + nums[i]
        return max(dp_max)

#方法2：dp_max[i]代表0~i可以打劫的最大金额，复杂度N
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp_max = [0]*len(nums)
        dp_max[0] = nums[0]
        dp_max[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp_max[i] = max(dp_max[i-2]+nums[i], dp_max[i-1])
        return max(dp_max)