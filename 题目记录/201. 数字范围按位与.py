class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 公共前缀后面补0
        bit = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            bit += 1
        return m << bit