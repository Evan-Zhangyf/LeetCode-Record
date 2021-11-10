class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        start = timeSeries[0]
        end = timeSeries[0] + duration - 1
        ans = 0
        for t in timeSeries:
            if t <= end + 1:
                end = max(end, t + duration - 1)
            else:
                ans += end - start + 1
                start = t
                end = t + duration - 1
        ans += end - start + 1
        return ans