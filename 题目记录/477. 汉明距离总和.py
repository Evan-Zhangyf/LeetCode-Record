class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cnt = [0] * 30
        for n in nums:
            for j in range(30):
                if n % 2:
                    cnt[j] += 1
                n = n >> 1
        ans = 0
        for c in cnt:
            ans += c * (len(nums) - c)
        return ans