class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        import heapq
        if k == 0:
            return []
        if len(arr) <= k:
            return arr
        h = [-arr[i] for i in range(k)]
        heapq.heapify(h)
        for i in range(k, len(arr)):
            if arr[i] < -h[0]:
                heapq.heapreplace(h, -arr[i])
        return [-n for n in h]
        