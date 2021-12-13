class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        west = []
        south = [0] * len(grid)
        # calculate skylines of west and south
        for i in range(len(grid)):
            west.append(max(grid[i]))
            for j in range(len(grid[0])):
                south[j] = max(south[j], grid[i][j])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(west[i] - grid[i][j], south[j] - grid[i][j])
        return ans