class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from collections import deque
        q = deque()
        q.append((0, 0, 1))
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        visited[0][0] = 1
        value = [matrix[0][0]]
        visited_num = 1
        previous_layer = 0
        while len(q) != 0:
            node = q.popleft()
            if node[2] != previous_layer and visited_num >= k:
                break
            previous_layer = node[2]
            if node[0] + 1 < len(matrix) and visited[node[0] + 1][node[1]] == 0:
                visited[node[0] + 1][node[1]] = 1
                value.append(matrix[node[0] + 1][node[1]])
                q.append((node[0] + 1, node[1], node[2] + 1))
            if node[1] + 1 < len(matrix[0]) and visited[node[0]][node[1] + 1] == 0:
                visited[node[0]][node[1] + 1] = 1
                value.append(matrix[node[0]][node[1] + 1])
                q.append((node[0], node[1] + 1, node[2] + 1))
        value.sort()
        print(value)
        return value[k-1]