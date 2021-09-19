class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = defaultdict(int)
        rides.sort(key = lambda x : x[1])
        dp[rides[0][1]] = rides[0][2] + rides[0][1] - rides[0][0]
        for i in range(1, len(rides)):
            if rides[i][1] != rides[i-1][1]:
                dp[rides[i][1]] = dp[rides[i-1][1]]
            if rides[0][1] > rides[i][0]:
                tmp = rides[i][2] + rides[i][1] - rides[i][0]
            else:
                l = 0
                r = i - 1
                while l < r:
                    m = (l + r + 1) // 2
                    if rides[m][1] > rides[i][0]:
                        r = m - 1
                    else:
                        l = m
                tmp = dp[rides[l][1]] + rides[i][2] + rides[i][1] - rides[i][0]
            dp[rides[i][1]] = max(dp[rides[i][1]], tmp)
        return dp[rides[-1][1]]