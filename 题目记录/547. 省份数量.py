class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        ans = 0
        for i in range(len(isConnected)):
            if visited[i] == False:
                ans += 1
                # dfs
                s = [i]
                visited[i] = True
                while len(s) != 0:
                    cur = s.pop()
                    for j in range(len(isConnected)):
                        if isConnected[cur][j] == 1 and visited[j] == False:
                            visited[j] = True
                            s.append(j)
        return ans