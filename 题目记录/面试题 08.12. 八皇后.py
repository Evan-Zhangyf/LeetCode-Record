class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        ans = []
        def check(state):
            if state == []:
                return True
            for line in range(len(state) - 1):
                for other in range(line + 1, len(state)):
                    # 检查列
                    if state[line] == state[other]:
                        return False
                    # 检查对角线
                    if state[line] + (other - line) == state[other] or state[line] - (other - line) == state[other]:
                        return False
            return True
        def back(state):
            if not check(state):
                return
            elif len(state) == n:
                temp_ans = []
                for i in range(n):
                    temp_ans.append((state[i] - 1) * "." + "Q" + (n - state[i]) * ".")
                ans.append(temp_ans)
                return
            else:
                for i in range(n):
                    back(state + [i + 1])
        back([])
        return ans