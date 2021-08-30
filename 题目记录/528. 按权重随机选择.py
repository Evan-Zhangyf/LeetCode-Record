class Solution:

    def __init__(self, w: List[int]):
        self.sum = [w[0]]
        for i in range(1, len(w)):
            self.sum.append(self.sum[-1] + w[i])
        


    def pickIndex(self) -> int:
        from random import randint
        rand = randint(1, self.sum[-1])
        l = 0
        r = len(self.sum) - 1
        while l < r:
            m = (l + r) // 2
            if self.sum[m] < rand:
                l = m + 1
            else:
                r = m
        return l




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()