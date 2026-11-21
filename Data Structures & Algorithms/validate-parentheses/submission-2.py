class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                continue
            if not stack:
                return False
            if ((stack[-1] == '(' and char == ')') or 
            (stack[-1] == '[' and char == ']') or 
            (stack[-1] == '{' and char == '}')):
                stack.pop()
            else:
                return False
        return not stack

        