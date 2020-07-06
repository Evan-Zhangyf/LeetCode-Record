class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[-1][-1] = 1
        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i + 1 <= len(obstacleGrid) - 1:
                    dp[i][j] += dp[i+1][j]
                if j + 1 <= len(obstacleGrid[0]) - 1:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]