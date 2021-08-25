class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def trace(routine):
            if routine[-1] == len(graph) - 1:
                ans.append(routine[:])
            for n in graph[routine[-1]]:
                routine.append(n)
                trace(routine)
                routine.pop()
        trace([0])
        return ans