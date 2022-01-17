class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        for t in timePoints:
            time.append(int(t[:2]) * 60 + int(t[3:]))
        time.sort()
        ans = min(abs(time[0] - time[-1]), 1440 - abs(time[0] - time[-1]))
        for i in range(1, len(time)):
            ans = min(min(abs(time[i] - time[i-1]), 1440 - abs(time[i] - time[i-1])), ans)
        return ans