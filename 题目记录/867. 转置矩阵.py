class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret[j].append(matrix[i][j])
        return ret