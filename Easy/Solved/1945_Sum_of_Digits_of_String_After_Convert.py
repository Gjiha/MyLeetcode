class Solution:
    def getLucky(self, s: str, k: int) -> int:
        newString = ''
        for char in s:
            newString += str(ord(char) -96)
        
        result = 0

        while k > 0:
            result = 0
            for digit in newString:
                result += int(digit)
            newString = str(result)
            k -= 1
        
        return result



sol = Solution()
print(sol.getLucky('leetcode',2))