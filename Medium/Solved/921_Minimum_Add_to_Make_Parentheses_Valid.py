class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        stack = []

        for bracket in string:
            if not stack:
                stack.append(bracket)
            else:
                if stack[-1] == '(' and bracket == ')':
                    stack.pop()
                else:
                    stack.append(bracket)
        
        return len(stack)

