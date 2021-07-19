class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        cur_sum = nums[0]
        while r < len(nums) - 1:
            if (r - l + 1) * nums[r + 1] - cur_sum <= k:
                r += 1
                cur_sum += nums[r]
            else:
                r += 1
                cur_sum += nums[r]
                cur_sum -= nums[l]
                l += 1
                
        return r - l + 1
