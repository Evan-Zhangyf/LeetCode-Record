class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]

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
            
        parent = [i for i in range(len(grid) * len(grid[0]))]
        edges = []
        # add and sort edges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # down
                if i != len(grid) - 1:
                    edges.append((i * len(grid[0]) + j, (i + 1) * len(grid[0]) + j, max(grid[i][j], grid[i+1][j])))
                # right
                if j != len(grid[0]) - 1:
                    edges.append((i * len(grid[0]) + j, i * len(grid[0]) + j + 1, max(grid[i][j], grid[i][j+1])))
        
        edges.sort(key = lambda x : x[2])

        # union
        for e in edges:
            union(e[0], e[1])
            if find(0) == find(len(grid) * len(grid[0]) - 1):
                return e[2]