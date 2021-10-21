class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        from collections import deque
        ans = 0
        q = deque([(0, 0)])
        visited = [False] * len(patience)
        visited[0] = True
        adj = [[] for _ in range(len(patience))]
        # construct graph
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        while q:
            cur = q.popleft()
            # calculate time
            if cur[0] != 0:
                tmp = ((cur[1] * 2 - 1) // patience[cur[0]]) * patience[cur[0]] + cur[1] * 2 + 1
                ans = max(ans, tmp)
            for n in adj[cur[0]]:
                if visited[n] == False:
                    visited[n] = True
                    q.append((n, cur[1] + 1))
        return ans