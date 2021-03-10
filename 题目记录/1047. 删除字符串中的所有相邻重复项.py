class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in range(len(S)):
            if stack == [] or stack[-1] != S[i]:
                stack.append(S[i])
            else:
                stack.pop()
        return "".join(stack)