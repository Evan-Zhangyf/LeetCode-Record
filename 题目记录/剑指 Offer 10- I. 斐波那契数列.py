class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev = 0
        cur = 1
        for i in range(n - 1):
            prev, cur = cur, (prev + cur) % (10**9 + 7)
        return cur
        