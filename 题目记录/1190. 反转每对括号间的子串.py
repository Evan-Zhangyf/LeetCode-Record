class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ")":
                stack.append(s[i])
            else:
                tmp = []
                while stack[-1] != "(":
                    tmp.append(stack.pop())
                stack.pop()
                for letter in tmp:
                    stack.append(letter)
        return "".join(stack)