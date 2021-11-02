class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        from collections import deque
        e = [[] for _ in range(n + 1)]
        vis = [False] * (n + 1)
        vis[1] = True
        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])
        e[1].append(1)
        q = deque([(1, 1)])
        for _ in range(t):
            for _ in range(len(q)):
                cur = q.popleft()
                cnt = 0
                for node in e[cur[0]]:
                    if vis[node] == False:
                        cnt += 1
                        vis[node] = True
                        q.append((node, cur[1] * (len(e[cur[0]]) - 1)))
                if cur[0] == target:
                    if cnt == 0:
                        return 1 / cur[1]
                    else:
                        return 0
        for i in range(len(q)):
            if q[i][0] == target:
                return 1 / q[i][1]
        return 0