import math as mt
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        strToControl = self.generateString(n)
        return strToControl[k-1]

    def generateString(self, n: int) -> str:
        if n == 1:
            return '0'
        preStr = self.generateString(n - 1)
        postStr = self.reverse(preStr)
        #print('pre: ',preStr)
        #print('post: ',postStr)
        return preStr + '1' + postStr

    def reverse(self, s:str) -> str:
        bin1 = int(s , base = 2)
        bin2 = (2**len(s) - 1)

        xorString = str(bin(bin1 ^ bin2))
        xorString = xorString[2:]

        return xorString[::-1]

sol = Solution()
print(sol.generateString(3))
