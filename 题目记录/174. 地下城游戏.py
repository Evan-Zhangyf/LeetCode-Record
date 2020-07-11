class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon[0])
        m = len(dungeon)
        dp = [[0]*n for i in range(m)]
        for i in range(m-1, -1, -1):
            for  j in range(n-1, -1, -1):
                dp_tmp = []
                if i != m-1:
                    dp_tmp.append(dp[i+1][j] - dungeon[i][j]) 
                if j != n-1:
                    dp_tmp.append(dp[i][j+1] - dungeon[i][j]) 
                if dp_tmp:
                    dp_tmp = [min(dp_tmp)]
                    dp_tmp.append(1)
                    dp[i][j] = max(dp_tmp)
                else:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
        return dp[0][0]