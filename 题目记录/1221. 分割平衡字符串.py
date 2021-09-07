class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_cnt = 0
        r_cnt = 0
        ans = 0
        for l in s:
            if l == "L":
                l_cnt += 1
            else:
                r_cnt += 1
            if l_cnt == r_cnt:
                ans += 1
        return ans