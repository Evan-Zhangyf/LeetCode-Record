class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def back(state, cur_sum):
            if cur_sum == target:
                ans.append(state)
                return
            for i in candidates:
                if i >= state[-1] and i + cur_sum <= target:
                    back(state + [i], i + cur_sum)
        for i in candidates:
            back([i], i)
        return ans