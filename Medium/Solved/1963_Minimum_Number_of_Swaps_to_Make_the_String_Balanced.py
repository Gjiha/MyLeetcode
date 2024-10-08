class Solution:
    def minSwaps(self, string: str) -> int:
        
        stack = []

        for bracket in string:
            if not stack:
                stack.append(bracket)
            else:
                if stack[-1] == '[' and bracket == ']':
                    stack.pop()
                else:
                    stack.append(bracket)
        
        if  len(stack) % 4 == 0:
            return len(stack)//4
        else:
            return len(stack)//4 + 1

sol = Solution()
print(sol.minSwaps("]]][[[")) 