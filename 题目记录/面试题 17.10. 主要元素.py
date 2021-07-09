class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1
            if cnt[i] > len(nums) // 2:
                return i
        return -1