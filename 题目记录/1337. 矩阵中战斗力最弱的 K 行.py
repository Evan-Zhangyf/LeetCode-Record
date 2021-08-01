class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        from math import ceil
        def power(row):
            if row[0] == 0:
                return -1
            l = 0
            r = len(row) - 1
            while l < r:
                m = ceil((l + r) / 2)
                if row[m] == 0:
                    r = m - 1
                else:
                    l = m
            return l
        import heapq
        h = []
        for i in range(k):
            h.append((-power(mat[i]), -i))
        heapq.heapify(h)
        for i in range(k, len(mat)):
            tmp = (-power(mat[i]), -i)
            if tmp > h[0]:
                heapq.heapreplace(h, tmp)
        ans = []
        for i in range(k):
            ans.append(-heapq.heappop(h)[1])
        ans.reverse()
        return ans
