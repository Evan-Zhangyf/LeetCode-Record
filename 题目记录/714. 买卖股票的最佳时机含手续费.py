class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][1] = - prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - fee + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]