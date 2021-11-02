class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        cnt = 0
        square_num = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                    visited[i][j] = True
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    square_num += 1
        
        ans = 0
        def back(pos):
            nonlocal ans
            nonlocal cnt
            if pos == end:
                if cnt == square_num:
                    ans += 1
                return
            directions = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
            for d in directions:
                if d[0] >= 0 and d[0] < len(grid) and d[1] >= 0 and d[1] < len(grid[0]) and grid[d[0]][d[1]] != -1 and visited[d[0]][d[1]] == False:
                    cnt += 1
                    visited[d[0]][d[1]] = True
                    back(d)
                    visited[d[0]][d[1]] = False
                    cnt -= 1
            return
        back(start)
        return ans
                