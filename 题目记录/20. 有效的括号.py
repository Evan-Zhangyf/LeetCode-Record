class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif stack:
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        if stack:
            return False
        else:
            return True
