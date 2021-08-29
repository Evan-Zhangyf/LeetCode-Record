class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = [0]
        for i in arr:
            sum.append(sum[-1] + i)
        ans = 0
        for l in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - l + 1):
                ans += sum[i + l] - sum[i]
        return ans