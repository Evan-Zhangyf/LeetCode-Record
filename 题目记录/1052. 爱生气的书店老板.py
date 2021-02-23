class Solution:
    def maxSatisfied(self, customers: List [int], grumpy: List[int], X: int) -> int:
        cur_sum = 0
        for i in range(X):
            cur_sum += customers[i]
        for i in range(X, len(customers)):
            if grumpy[i] == 0:
                cur_sum += customers[i]
        ret = cur_sum
        for i in range(len(customers) - X):
            cur_sum = cur_sum - grumpy[i] * customers[i] + grumpy[i + X] * customers[i + X]
            ret = max(cur_sum, ret)
        return ret