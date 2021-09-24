class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        abs_min = float("inf")
        negative_cnt = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                ans += abs(matrix[i][j])
                abs_min = min(abs(matrix[i][j]), abs_min)
                if matrix[i][j] < 0:
                    negative_cnt += 1

        if negative_cnt % 2 == 0:
            return ans
        else:
            return ans - 2 * abs_min