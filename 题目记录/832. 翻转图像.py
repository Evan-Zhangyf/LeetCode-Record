class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range(len(A[0]) // 2):
                A[i][j], A[i][len(A[0]) - 1 - j] = A[i][len(A[0]) - 1 - j], A[i][j]
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = 1 - A[i][j]
        return A