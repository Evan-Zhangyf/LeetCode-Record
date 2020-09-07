class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        hash_map = {}
        for i in nums:
            if hash_map.get(i) == None:
                hash_map[i] = [1, False]
            else:
                hash_map[i][0] += 1
        nums_list = []
        for i in nums:
            if hash_map[i][1] == False:
                nums_list.append((hash_map[i][0], i))
                hash_map[i][1] = True
        heap = nums_list[:k]
        heapq.heapify(heap)
        for i in nums_list[k:]:
            if i > heap[0]:
                heapq.heapreplace(heap, i)
        return [i[1] for i in heap]