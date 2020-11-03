class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        top = 9999999999
        twist = False
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                return False
            if (not twist) and A[i-1] > A[i]:
                twist = True
                top = i - 1
            if twist and A[i-1] < A[i]:
                return False
        return top < len(A) - 1 and top > 0