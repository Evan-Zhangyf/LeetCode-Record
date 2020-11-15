class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = [num[0]]
        for i in range(1, len(num)):
            if num[i] > num[i-1]:
                s.append(num[i])
            else:
                while k > 0 and len(s) != 0 and num[i] < s[-1]:
                    s.pop()
                    k -= 1
                s.append(num[i])
        for i in range(k):
            s.pop()
        s = "".join(s)
        if s == "":
            return "0"
        for i in range(len(s)-1):
            if s[i] != "0":
                return s[i:]
        return s[-1]