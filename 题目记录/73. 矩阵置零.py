class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_dic = [False] * len(matrix)
        col_dic = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_dic[i] = True
                    col_dic[j] = True
        for i in range(len(row_dic)):
            if row_dic[i]:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(len(col_dic)):
            if col_dic[j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
