class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        pop_ptr = 0
        for i in pushed:
            s.append(i)
            while s and s[-1] == popped[pop_ptr]:
                s.pop()
                pop_ptr += 1
        return pop_ptr == len(popped)
