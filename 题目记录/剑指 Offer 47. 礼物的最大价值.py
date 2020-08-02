class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmp = 0
                if i - 1 >= 0:
                    tmp = dp[i-1][j]
                if j - 1 >= 0:
                    tmp = max(tmp, dp[i][j-1])
                dp[i][j] = tmp + grid[i][j]
        return dp[-1][-1]