class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        ans = []
        
        def back(num_list):
            if len(num_list) == k:
                ans.append(num_list)
                return
            for i in range(num_list[-1] + 1, n + 1):
                back(num_list + [i])
        
        for i in range(1, n + 1):
            back([i])
        return ans