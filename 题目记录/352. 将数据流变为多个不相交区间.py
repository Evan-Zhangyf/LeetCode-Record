class SummaryRanges:

    def __init__(self):
        self.interval = []

    def addNum(self, val: int) -> None:
        if self.interval == []:
            self.interval.append([val, val])
            return
        if self.interval[0][0] - 1 == val:
            # coalesce
            self.interval[0][0] -= 1
            return
        if self.interval[0][0] > val:
            self.interval.insert(0, [val, val])
            return
        
        # binary search
        l = 0
        r = len(self.interval) - 1
        while l < r:
            m = (l + r + 1) // 2
            if self.interval[m][0] > val:
                r = m - 1
            else:
                l = m
        if self.interval[l][1] >= val:
            return
        if self.interval[l][1] + 1 == val:
            self.interval[l][1] += 1
            if l != len(self.interval) - 1 and self.interval[l+1][0] == self.interval[l][1] + 1:
                # coalesce
                self.interval[l][1] = self.interval[l+1][1]
                del self.interval[l+1]
            return
        if l != len(self.interval) - 1 and self.interval[l+1][0] - 1 == val:
            # coalesce
            self.interval[l+1][0] -= 1
            return
        self.interval.insert(l + 1, [val ,val])
        return


    def getIntervals(self) -> List[List[int]]:
        return self.interval



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()