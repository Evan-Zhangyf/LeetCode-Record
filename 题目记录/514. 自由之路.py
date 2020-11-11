class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [[-1] * len(ring) for _ in range(len(key))]
        dic = {}
        for i in range(len(ring)):
            if dic.get(ring[i]):
                dic[ring[i]].append(i)
            else:
                dic[ring[i]] = [i]

        for i in dic[key[0]]:
            dp[0][i] = min(i, len(ring) - i) + 1

        for i in range(1, len(key)):
            for j in dic[key[i]]:
                tmp = 9999999
                for k in dic[key[i-1]]:
                    tmp = min(tmp, dp[i-1][k] + min((j - k) % len(ring), len(ring) - (j - k) % len(ring)))
                dp[i][j] = tmp + 1
        
        ret = 9999999
        for i in dic[key[-1]]:
            ret = min(ret, dp[len(key)-1][i])
        return ret