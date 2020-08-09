class Solution:
    def myPow(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if n % 2 == 0:
            tmp = self.myPow(x, n / 2)
            return tmp * tmp
        else:
            tmp = self.myPow(x, (n - 1) / 2)
            return x * tmp * tmp