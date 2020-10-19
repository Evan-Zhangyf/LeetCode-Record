class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        tmp_s = []
        tmp_t = []
        for i in S:
            if i == "#":
                if len(tmp_s) > 0:
                    tmp_s.pop()
            else:
                tmp_s.append(i)
        for i in T:
            if i == "#":
                if len(tmp_t) > 0:
                    tmp_t.pop()
            else:
                tmp_t.append(i)
        return tmp_s == tmp_t