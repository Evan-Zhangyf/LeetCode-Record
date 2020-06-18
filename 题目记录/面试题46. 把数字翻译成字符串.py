class Solution:
    def translateNum(self, num: int) -> int:
        if num == []:
            return 0
        num = str(num)
        dp = [0] * (len(num)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(num)+1):
            if int(num[i-2:i]) <= 25 and int(num[i-2:i]) >= 10:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[len(num)]