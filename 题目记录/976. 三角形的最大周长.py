class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        ans = 0
        A.sort()
        for i in range(len(A)-1,1,-1):
            if A[i] < A[i-1] + A[i-2]:
                ans = A[i] + A[i-1] + A[i-2]
                break
        return ans