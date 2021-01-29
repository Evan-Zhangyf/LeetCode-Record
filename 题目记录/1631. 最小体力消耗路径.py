class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if len(heights) == 1 and len(heights[0]) == 1:
            return 0

        def find(pos):
            while parent[pos] != pos:
                parent[pos] = parent[parent[pos]]
                pos = parent[pos]
            return pos

        def union(pos1, pos2):
            parent1 = find(pos1)
            parent2 = find(pos2)
            if parent1 == parent2:
                return
            else:
                parent[parent1] = parent2
            
        parent = [i for i in range(len(heights) * len(heights[0]))]
        edges = []
        # add and sort edges
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # down
                if i != len(heights) - 1:
                    edges.append((i * len(heights[0]) + j, (i + 1) * len(heights[0]) + j, abs(heights[i][j] - heights[i+1][j])))
                # right
                if j != len(heights[0]) - 1:
                    edges.append((i * len(heights[0]) + j, i * len(heights[0]) + j + 1, abs(heights[i][j] - heights[i][j+1])))
        
        edges.sort(key = lambda x : x[2])

        # union
        for e in edges:
            union(e[0], e[1])
            if find(0) == find(len(heights) * len(heights[0]) - 1):
                return e[2]
