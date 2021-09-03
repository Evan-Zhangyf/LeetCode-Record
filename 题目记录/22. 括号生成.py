class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = 0
        right = 0
        ans = []
        def check(state):
            s = []
            for sign in state:
                if sign == "(":
                    s.append(sign)
                else:
                    if len(s) == 0:
                        return False
                    s.pop()
            return True

        def back(state):
            nonlocal left
            nonlocal right
            if check(state) == False:
                return
            if len(state) == n * 2:
                ans.append("".join(state))
                return
            if left < n:
                left += 1
                state.append("(")
                back(state)
                state.pop()
                left -= 1
            if right < n:
                right += 1
                state.append(")")
                back(state)
                state.pop()
                right -= 1
        back([])
        return ans