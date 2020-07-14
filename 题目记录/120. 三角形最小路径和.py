class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # O(N)额外空间
        # 特判
        if len(triangle) == 1:
            return triangle[0][0]
        
        pre_line = triangle[0]
        for i in range(1, len(triangle)):
            cur_line = [0] * len(triangle[i])
            cur_line[0] = triangle[i][0] + pre_line[0]
            for j in range(1, len(triangle[i]) - 1):
                cur_line[j] = triangle[i][j] + min(pre_line[j-1], pre_line[j])
            cur_line[-1] = triangle[i][-1] + pre_line[-1]
            pre_line = cur_line
        return min(cur_line)