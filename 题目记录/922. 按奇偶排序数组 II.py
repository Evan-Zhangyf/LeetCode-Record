class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_idx = []
        even_idx = []
        for i in range(len(A)):
            if A[i] % 2 == 1:
                odd_idx.append(i)
            else:
                even_idx.append(i)
        ret = [0] * len(A)
        for i in range(len(A)):
            if i % 2 == 1:
                ret[i] = A[odd_idx[i//2]]
            else:
                ret[i] = A[even_idx[i//2]]
        return ret