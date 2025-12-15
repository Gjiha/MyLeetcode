class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        n = len(prices)
        returnValue = n
        count = 1
        
        for i in range(1,n):
            if prices[i] == prices[i-1] - 1:
                count += 1
            else:
                if count > 1:
                    returnValue = returnValue+(((count)*(count-1)//2))
                    count = 1

        if count > 1:
            returnValue = returnValue+(((count)*(count-1)//2))
            count = 1
        
        return returnValue
        
sol = Solution()
print(sol.getDescentPeriods([8,6,7,7]))