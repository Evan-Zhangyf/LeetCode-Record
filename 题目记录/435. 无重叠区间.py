class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 有意义的模板，最大无重叠区间问题
        if intervals == []:
            return 0
        intervals.sort(key=lambda x : x[1])
        cur = intervals[0]
        ans = len(intervals) - 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= cur[1]:
                ans -= 1
                cur = intervals[i]
        return ans
