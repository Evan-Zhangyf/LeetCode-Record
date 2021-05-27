class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        tmp = x ^ y
        while tmp != 0:
            ans += tmp & 1
            tmp = tmp >> 1
        return ans