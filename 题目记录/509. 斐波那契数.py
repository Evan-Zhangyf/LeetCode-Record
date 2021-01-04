class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        fib1 = 0
        fib2 = 1
        ans = 1
        for i in range(n-2):
            fib1, fib2 = fib2, ans
            ans = fib1 + fib2
        return ans