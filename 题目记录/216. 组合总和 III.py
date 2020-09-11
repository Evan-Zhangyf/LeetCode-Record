class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def back(state, cur_sum):
            if len(state) == k:
                if cur_sum == n:
                    ans.append(state)
                    return
                return
            for i in range(state[-1] + 1, 10):
                if i + cur_sum <= n:
                    back(state + [i], i + cur_sum)
        for i in range(1, 10):
            back([i], i)
        return ans