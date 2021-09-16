class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x : x[0])
        ans = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[i][1])
            else:
                ans.append(cur)
                cur = intervals[i]
        ans.append(cur)
        return ans