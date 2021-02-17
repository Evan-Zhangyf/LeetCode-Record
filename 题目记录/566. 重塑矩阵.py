class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        ans = [[] for _ in range(r)]
        x = 0
        y = 0
        for i in range(r):
            for j in range(c):
                ans[i].append(nums[x][y])
                y += 1
                if y == len(nums[0]):
                    x += 1
                    y = 0
        return ans