class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        h = []
        ans = 0
        for i in range(len(apples)):
            if apples[i] > 0:
                heapq.heappush(h, (i + days[i], apples[i]))
            # pop rotten apples
            while len(h) > 0 and h[0][0] <= i:
                heapq.heappop(h)
            # eat apple
            if len(h) > 0:
                if h[0][1] > 1:
                    heapq.heapreplace(h, (h[0][0], h[0][1] - 1))
                else:
                    heapq.heappop(h)
                ans += 1
        day = len(apples)
        while len(h):
            # pop rotten apples
            while len(h) > 0 and h[0][0] <= day:
                heapq.heappop(h)
            # eat apple
            if len(h) > 0:
                if h[0][1] > 1:
                    heapq.heapreplace(h, (h[0][0], h[0][1] - 1))
                else:
                    heapq.heappop(h)
                ans += 1
            day += 1
        return ans
