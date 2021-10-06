class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        import heapq
        h = [nums[0]]
        for i in range(1, len(nums)):
            if not nums[i] in h:
                if len(h) < 3:
                    heapq.heappush(h, nums[i])
                elif nums[i] > h[0]:
                    heapq.heapreplace(h, nums[i])
        if len(h) < 3:
            return max(h)
        else:
            return h[0]