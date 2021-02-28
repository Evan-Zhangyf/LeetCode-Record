class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                dec = False
            if A[i] < A[i-1]:
                inc = False
            if not dec and not inc:
                return False
        return True