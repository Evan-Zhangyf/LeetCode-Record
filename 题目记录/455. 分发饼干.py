class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        s.sort()
        g.sort()
        ans = 0
        j = 0
        for i in g:
            while s[j] < i:
                j += 1
                if j == len(s):
                    return ans
            ans += 1
            j += 1
            if j == len(s):
                return ans
        return ans