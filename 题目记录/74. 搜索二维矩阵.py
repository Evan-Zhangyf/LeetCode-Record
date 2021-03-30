class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0])
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
                left = mid + 1
            else:
                right = mid
        if left > len(matrix) * len(matrix[0]) - 1:
            return False
        else:
            if matrix[left // len(matrix[0])][left % len(matrix[0])] == target:
                return True
            else:
                return False
        