class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt
        for i in range(int(sqrt(c / 2)) + 1):
            if sqrt(c - i * i) % 1 == 0:
                return True
        return False