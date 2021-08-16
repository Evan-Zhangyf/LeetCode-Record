class Solution:
    def countArrangement(self, n: int) -> int:
        vis = n * [0]
        ans = 0
        def back(state):
            nonlocal ans
            if state == n:
                ans += 1
                return
            for i in range(n):
                if vis[i] == False and ((state + 1) % (i + 1) == 0 or (i + 1) % (state + 1) == 0):
                    vis[i] = True
                    back(state + 1)
                    vis[i] = False
        
        back(0)
        return ans 