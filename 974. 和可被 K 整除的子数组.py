class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        #r[i]为余数为i的数的个数
        r = [0] * K
        r[0] = 1
        cur_sum = 0
        count = 0
        for i in A:
            cur_sum += i
            count += r[cur_sum%K]
            r[cur_sum%K] += 1
        return count