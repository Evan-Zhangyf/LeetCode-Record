class Solution:
    def minSwaps(self, s: str) -> int:
        cnt1 = 0
        for i in range(len(s)):
            if s[i] == "1":
                cnt1 += 1
        if abs(cnt1 * 2 - len(s)) > 1:
            return -1
        cur = "0"
        diff = 0
        for i in range(len(s)):
            if s[i] != cur:
                diff += 1
            if cur == "0":
                cur = "1"
            else:
                cur = "0"
        if len(s) % 2 == 0:
            return min(diff, len(s) - diff) // 2
        else:
            if cnt1 * 2 > len(s):
                return (len(s) - diff) // 2
            else:
                return diff // 2