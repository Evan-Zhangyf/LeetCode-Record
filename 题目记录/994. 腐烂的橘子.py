class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        cnt = 0
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        time = 0
        while q:
            row, col, t = q.popleft()
            time = max(time, t)
            # up
            if row > 0 and grid[row-1][col] == 1:
                cnt -= 1
                grid[row-1][col] = 2
                q.append((row - 1, col, t + 1))
            # down
            if row < len(grid) - 1 and grid[row+1][col] == 1:
                cnt -= 1
                grid[row+1][col] = 2
                q.append((row + 1, col, t + 1))
            # left
            if col > 0 and grid[row][col-1] == 1:
                cnt -= 1
                grid[row][col-1] = 2
                q.append((row, col - 1, t + 1))
            # right
            if col < len(grid[0]) - 1 and grid[row][col+1] == 1:
                cnt -= 1
                grid[row][col+1] = 2
                q.append((row, col + 1, t + 1))
        if cnt == 0:
            return time
        else:
            return -1
            