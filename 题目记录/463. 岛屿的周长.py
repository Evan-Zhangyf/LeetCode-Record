class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # up
                    if i == 0 or grid[i-1][j] == 0:
                        p += 1
                    # down
                    if i == len(grid) - 1 or grid[i+1][j] == 0:
                        p += 1
                    # left
                    if j == 0 or grid[i][j-1] == 0:
                        p += 1
                    # right
                    if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                        p += 1
        return p