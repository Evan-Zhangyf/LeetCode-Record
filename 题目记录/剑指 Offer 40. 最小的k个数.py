class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        import heapq
        ans = [-arr[i] for i in range(k)]
        heapq.heapify(ans)
        for i in range(k, len(arr)):
            if -arr[i] > ans[0]:
                heapq.heapreplace(ans, -arr[i])
        return [-i for i in ans]