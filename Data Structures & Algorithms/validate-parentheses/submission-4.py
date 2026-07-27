class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        if(len(s) == 0):
            return False

        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else: 
                    return False


        return len(stack) == 0