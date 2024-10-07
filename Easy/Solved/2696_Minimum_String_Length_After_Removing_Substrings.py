class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if stack == []:
                stack.append(char)
            
            elif char == 'D' and stack[-1] == 'C':
                stack.pop()
            
            elif char == 'B' and stack[-1] == 'A':
                stack.pop()
            
            else:
                stack.append(char)
        
        return len(stack)

sol = Solution()
x = "ABFCACDB"
print(sol.minLength(x))


            

        