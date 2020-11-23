class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []:
            return 0
        points.sort(key = lambda x : x[1])
        cnt = 1
        arrow = points[0][1]
        for i in range(len(points)):
            if points[i][0] > arrow:
                cnt += 1
                arrow = points[i][1]
        return cnt