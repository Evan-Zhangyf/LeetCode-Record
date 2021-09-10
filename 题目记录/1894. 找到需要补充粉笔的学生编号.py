class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = 0
        for i in range(len(chalk)):
            prefix_sum += chalk[i]
            chalk[i] = prefix_sum
        k %= chalk[-1]
        l = 0
        r = len(chalk) - 1
        while l < r:
            m = (l + r) // 2
            if chalk[m] <= k:
                l = m + 1
            else:
                r = m
        return l