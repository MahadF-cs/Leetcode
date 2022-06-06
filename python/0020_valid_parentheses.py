from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack[-1]
                if top == '(' and char != ')':
                    return False
                elif top == '{' and char != '}':
                    return False
                elif top == '[' and char != ']':
                    return False
                stack.pop()
                
        return len(stack) == 0
