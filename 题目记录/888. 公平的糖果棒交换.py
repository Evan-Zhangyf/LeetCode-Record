class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = 0
        sum_B = 0
        dic_B = {}
        for i in A:
            sum_A += i
        for i in B:
            sum_B += i
            dic_B[i] = True
        diff = sum_A - sum_B
        for i in A:
            if dic_B.get(i - diff / 2):
                return [i, int(i - diff / 2)]