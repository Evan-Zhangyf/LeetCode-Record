class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        # color为0代表未访问，正负1为2种颜色
        color = [0] * len(graph)
        q = deque()
        for node in range(len(graph)):
            if color[node] == 0:
                q.append(node)
                color[node] = 1
                while len(q) != 0:
                    cur = q.popleft()
                    for i in graph[cur]:
                        if color[i] == 0:
                            q.append(i)
                            color[i] = -color[cur]
                        elif color[i] == color[cur]:
                            return False
        return True