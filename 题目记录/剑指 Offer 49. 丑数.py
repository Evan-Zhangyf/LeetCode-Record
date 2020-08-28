class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 三指针
        ptr1 = 0
        ptr2 = 0
        ptr3 = 0
        dp = [1] * n
        for i in range(1, n):
            dp[i] = min(2 * dp[ptr1], 3 * dp[ptr2], 5 * dp[ptr3])
            # 更新指针
            while ptr1 <= i and dp[ptr1] * 2 <= dp[i]:
                ptr1 += 1
            while ptr2 <= i and dp[ptr2] * 3 <= dp[i]:
                ptr2 += 1
            while ptr3 <= i and dp[ptr3] * 5 <= dp[i]:
                ptr3 += 1
        return dp[-1]