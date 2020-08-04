class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        # 计算入度
        in_deg = [0] * numCourses
        for edge in prerequisites:
            in_deg[edge[0]] += 1

        # 拓扑排序
        num = 0
        q = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)
                num += 1
        while len(q) != 0:
            cur_node = q.popleft()
            for edge in prerequisites:
                if edge[1] == cur_node:
                    in_deg[edge[0]] -= 1
                    if in_deg[edge[0]] == 0:
                        q.append(edge[0])
                        num += 1
        return num == numCourses
