class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = [0] * 60
        ans = 0
        for t in time:
            ans += rem[(60 - t % 60) % 60]
            rem[t % 60] += 1
        return ans