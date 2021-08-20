class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s, l, r):
            for i in range((r - l + 1) // 2):
                s[l+i], s[r-i] = s[r-i], s[l+i]
        
        s = list(s)
        rem = len(s)
        cur = 0
        while rem >= 2 * k:
            rem -= 2 * k
            reverse(s, cur, cur + k - 1)
            cur += 2 * k
        if rem < k:
            reverse(s, cur, len(s) - 1)
        else:
            reverse(s, cur, cur + k - 1)
        return "".join(s)
