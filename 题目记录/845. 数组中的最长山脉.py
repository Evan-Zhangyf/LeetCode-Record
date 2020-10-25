class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        up_dp = [1] * len(A)
        down_dp = [1] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                up_dp[i] = up_dp[i-1] + 1
                down_dp[i] = 1
            elif A[i] < A[i-1]:
                down_dp[i] = down_dp[i-1] + 1
                up_dp[i] = 1
            else:
                up_dp[i] = 1
                down_dp[i] = 1
        ans = 0
        for i in range(2, len(A)):
            if down_dp[i] > 1 and up_dp[i - down_dp[i] + 1] > 1:
                tmp = down_dp[i] + up_dp[i - down_dp[i] + 1] - 1
                if tmp >= 3:
                    ans = max(ans, tmp)
        return ans