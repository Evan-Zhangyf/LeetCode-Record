class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #最小堆
        import heapq
        heap = nums[0:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]