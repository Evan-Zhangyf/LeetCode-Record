class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        cur = []
        ans = []
        def back(pos):
            if pos == len(num) - 1:
                tmp = "".join(cur)
                if eval(tmp) == target:
                    ans.append(tmp)
                return
            flag = True
            i = len(cur) - 1
            while i >= 0:
                if cur[i] == "+" or cur[i] == "-" or cur[i] == "*":
                    break
                i -= 1
            if i != len(cur) - 1 and cur[i+1] == "0":
                flag = False
            if flag:
                cur.append(num[pos+1])
                back(pos + 1)
                cur.pop()
            if pos == -1:
                return
            # +
            cur.append("+")
            cur.append(num[pos+1])
            back(pos + 1)
            cur.pop()
            cur.pop()
            # -
            cur.append("-")
            cur.append(num[pos+1])
            back(pos + 1)
            cur.pop()
            cur.pop()
            # *
            cur.append("*")
            cur.append(num[pos+1])
            back(pos + 1)
            cur.pop()
            cur.pop()
        back(-1)
        return ans