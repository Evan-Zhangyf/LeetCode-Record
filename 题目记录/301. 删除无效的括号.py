class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        visited = set()
        ans = []
        cur = []
        left = 0
        right = 0
        for l in s:
            if l == "(":
                left += 1
            if l == ")":
                right += 1
        thres = min(left, right)
        left = 0
        right = 0
        def back(pos):
            nonlocal ans, left, right
            if pos == len(s):
                tmp = "".join(cur)
                if tmp in visited:
                    return
                else:
                    visited.add(tmp)
                if left == right:
                    if len(ans) == 0 or len(cur) == len(ans[0]):
                        ans.append("".join(cur))
                    elif len(cur) > len(ans[0]):
                        ans = ["".join(cur)]
                return

            # pruning
            if left > thres or right > thres:
                return
            if abs(left - right) > len(s) - pos:
                return

            if s[pos] == ')':
                if left < right:
                    return
                elif left > right:
                    right += 1
                    cur.append(')')
                    back(pos + 1)
                    cur.pop()
                    right -= 1
            elif s[pos] == '(':
                left += 1
                cur.append('(')
                back(pos + 1)
                cur.pop()
                left -= 1
            else:
                cur.append(s[pos])
                back(pos + 1)
                cur.pop()
            back(pos + 1)
        
        back(0)
        return ans