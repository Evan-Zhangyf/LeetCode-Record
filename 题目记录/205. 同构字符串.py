class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        mapped = {}
        tmp = []
        for i in range(len(s)):
            if dic.get(s[i]):
                if dic[s[i]] != t[i]:
                    return False
            else:
                if mapped.get(t[i]):
                        return False
                else:
                    dic[s[i]] = t[i]
                    mapped[t[i]] = True
        return True