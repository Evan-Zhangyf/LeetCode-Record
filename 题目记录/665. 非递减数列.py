class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        gap_cnt = 0
        gap_flag = 0
        for i in range(1, len(nums)):
            if gap_flag == 1:
                if nums[i] < nums[i-2] and i >= 3 and nums[i-1] < nums[i-3]:
                    return False
                gap_flag = 0
            if nums[i] < nums[i-1]:
                gap_cnt += 1
                if gap_cnt > 1:
                    return False
                gap_flag = 1
        return True