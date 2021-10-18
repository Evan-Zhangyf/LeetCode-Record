class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        base = 1
        while num:
            ans += abs(num % 2 - 1) * base
            num = num // 2
            base *= 2
        return ans