class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        nums.reverse()
        s = 0
        for i in nums:
            s += i
        if s % k:
            return False
        target = s // k
        subset = [0] * k
        def back(pos):
            if pos == len(nums):
                return True
            for i in range(k):
                if subset[i] + nums[pos] <= target:
                    subset[i] += nums[pos]
                    if back(pos + 1):
                        return True
                    subset[i] -= nums[pos]
            return False
        return back(0)