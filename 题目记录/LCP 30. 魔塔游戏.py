class Solution:
    def magicTower(self, nums: List[int]) -> int:
        hp = 1
        for i in nums:
            hp += i
        if hp <= 0:
            return -1
        import heapq
        h = []
        hp = 1
        cnt = 0
        for i in nums:
            if i < 0:
                heapq.heappush(h, i)
            hp += i
            if hp <= 0:
                hp -= heapq.heappop(h)
                cnt += 1
        return cnt