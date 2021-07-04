class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        max_val = len(nums)
        for i in nums:
            cnt[i] += 1
        ans = [0, 0]
        for i in range(1, max_val + 1):
            if cnt[i] == 2:
                ans[0] = i
            if cnt[i] == 0:
                ans[1] = i
        return ans