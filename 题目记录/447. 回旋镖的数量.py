class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            dic = defaultdict(int)
            for j in range(len(points)):
                dic[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2] += 1
            for v in dic.values():
                ans += v * (v - 1)
        return ans