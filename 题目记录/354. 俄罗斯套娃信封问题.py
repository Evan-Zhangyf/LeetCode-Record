class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        dp = [envelopes[0][1]]
        for i in range(len(envelopes)):
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                left = 0
                right = len(dp)
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[mid] < envelopes[i][1]:
                        left = mid + 1
                    else:
                        right = mid
                dp[left] = envelopes[i][1]
        return len(dp)