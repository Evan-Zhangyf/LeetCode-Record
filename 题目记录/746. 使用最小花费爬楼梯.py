class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        for i in range(len(cost) - 1, -1, -1):
            if i == len(cost) - 1 or i == len(cost) - 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        return min(dp[0], dp[1])