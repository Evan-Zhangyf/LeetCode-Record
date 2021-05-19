class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        h = []
        flag = False
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp1 = 0
                tmp2 = 0
                tmp3 = 0
                if i >= 1:
                    tmp1 = dp[i-1][j]
                if j >= 1:
                    tmp2 = dp[i][j-1]
                if i >= 1 and j >= 1:
                    tmp3 = dp[i-1][j-1]
                dp[i][j] = tmp1 ^ tmp2 ^ tmp3 ^ matrix[i][j]
                if flag == False:
                    h.append(dp[i][j])
                    if len(h) == k:
                        flag = True
                        heapq.heapify(h)
                else:
                    if dp[i][j] > h[0]:
                        heapq.heapreplace(h, dp[i][j])
        return h[0]


                