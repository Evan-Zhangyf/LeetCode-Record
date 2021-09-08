class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        import heapq
        h = [int(nums[i]) for i in range(k)]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            tmp = int(nums[i])
            if tmp > h[0]:
                heapq.heapreplace(h, tmp)
        return str(h[0])