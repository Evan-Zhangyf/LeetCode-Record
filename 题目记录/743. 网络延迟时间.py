class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for e in times:
            adj[e[0] - 1].append((e[1] - 1, e[2]))
        dis = [10001] * n
        dis[k - 1] = 0
        for e in adj[k - 1]:
            dis[e[0]] = e[1]
        vis = [False] * n
        vis[k - 1] = True
        for _ in range(n - 1):
            min_val = 10002
            for i in range(n):
                if vis[i] == False and dis[i] < min_val:
                    cur = i
                    min_val = dis[i]
            vis[cur] = True
            for e in adj[cur]:
                if vis[e[0]] == False and e[1] + dis[cur] < dis[e[0]]:
                    dis[e[0]] = e[1] + dis[cur]
        ans = max(dis)
        if ans == 10001:
            return -1
        else:
            return ans