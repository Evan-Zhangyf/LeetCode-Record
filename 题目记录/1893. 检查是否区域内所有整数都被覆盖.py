class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for l in ranges:
            diff[l[0]] += 1
            diff[l[1] + 1] -= 1
        cur = 0
        for i in range(1, right + 1):
            cur += diff[i]
            if i >= left and cur <= 0:
                return False
        return True