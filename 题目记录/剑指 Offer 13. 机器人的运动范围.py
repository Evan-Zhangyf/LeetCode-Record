class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if m == 0 or n == 0:
            return 0
        def digit_sum(cur):
            a = cur[0]
            b = cur[1]
            ret = 0
            while a != 0:
                ret += a % 10
                a = a // 10
            while b != 0:
                ret += b % 10
                b = b // 10
            return ret
        from collections import deque
        q = deque([[0, 0]])
        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1
        ans = 0
        while len(q) != 0:
            cur = q.popleft()
            ans += 1
            # up
            if cur[0] - 1 >= 0 and visited[cur[0] - 1][cur[1]] == 0 and digit_sum([cur[0] - 1, cur[1]]) <= k:
                visited[cur[0] - 1][cur[1]] = 1
                q.append([cur[0] - 1, cur[1]])
            # down
            if cur[0] + 1 < m and visited[cur[0] + 1][cur[1]] == 0 and digit_sum([cur[0] + 1, cur[1]]) <= k:
                visited[cur[0] + 1][cur[1]] = 1
                q.append([cur[0] + 1, cur[1]])
            # left
            if cur[1] - 1 >= 0 and visited[cur[0]][cur[1] - 1] == 0 and digit_sum([cur[0], cur[1] - 1]) <= k:
                visited[cur[0]][cur[1] - 1] = 1
                q.append([cur[0], cur[1] - 1])
            # right
            if cur[1] + 1 < n and visited[cur[0]][cur[1] + 1] == 0 and digit_sum([cur[0], cur[1] + 1]) <= k:
                visited[cur[0]][cur[1] + 1] = 1
                q.append([cur[0], cur[1] + 1])
        return ans