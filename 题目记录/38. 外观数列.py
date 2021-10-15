class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        num = self.countAndSay(n - 1)
        cnt = 1
        ret = []
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cnt += 1
            else:
                ret.append(str(cnt))
                ret.append(str(num[i-1]))
                cnt = 1
        ret.append(str(cnt))
        ret.append(str(num[-1]))
        return "".join(ret)
