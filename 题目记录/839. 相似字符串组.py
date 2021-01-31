class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(s):
            while parent[s] != s:
                parent[s] = parent[parent[s]]
                s = parent[s]
            return s

        def union(s1, s2):
            nonlocal cnt
            parent1 = find(s1)
            parent2 = find(s2)
            if parent1 == parent2:
                return
            else:
                cnt -= 1
                parent[parent1] = parent2

        def similar(s1, s2):
            n = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    n += 1
            return n == 2 or n == 0

        cnt = len(strs)
        parent = []
        for i in range(len(strs)):
            parent.append(i)

        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                if similar(strs[i], strs[j]):
                    union(i, j)
        return cnt
        