class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        cur = target
        for i in range(maxDoubles):
            if cur == 1:
                return ans
            if cur % 2 == 1:
                ans += 2
            else:
                ans += 1
            cur = cur // 2
        ans += cur - 1
        return ans