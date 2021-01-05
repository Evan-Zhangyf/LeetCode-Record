class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        begin = 0
        for i in range(len(s)):
            if i != 0 and s[i-1] != s[i]:
                if i - begin >= 3:
                    ans.append([begin, i - 1])
                begin = i
        if len(s) - begin >= 3:
            ans.append([begin, len(s) - 1])
        ans.sort(key = lambda x : x[0])
        return ans