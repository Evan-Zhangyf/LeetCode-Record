class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dic = defaultdict(int)
        for rec in rectangles:
            dic[rec[0]/rec[1]] += 1
        ans = 0
        for v in dic.values():
            ans += int(v * (v - 1) / 2)
        return ans