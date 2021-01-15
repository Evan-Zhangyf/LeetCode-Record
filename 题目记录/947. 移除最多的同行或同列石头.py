class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #并查集函数
        def find(pos):
            while parent[pos] != pos:
                parent[pos] = parent[parent[pos]]
                pos = parent[pos]
            return pos

        def union(pos1, pos2):
            nonlocal cnt
            parent1 = find(pos1)
            parent2 = find(pos2)
            if parent1 != parent2:
                parent[parent1] = parent2
                cnt -= 1

        cnt = len(stones)
        parent = {}
        for i in range(len(stones)):
            stones[i] = tuple(stones[i])
            parent[stones[i]] = stones[i]
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(stones[i], stones[j])
        return len(stones) - cnt