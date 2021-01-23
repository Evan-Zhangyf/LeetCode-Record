class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 定义并查集
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            nonlocal cnt
            p1 = find(x)
            p2 = find(y)
            if p1 == p2:
                return
            else:
                parent[p1] = p2
                cnt -= 1
        
        if len(connections) < n - 1:
            return -1
        cnt = n
        parent = []
        for i in range(n):
            parent.append(i)
        for edge in connections:
            union(edge[0], edge[1])
        return cnt - 1