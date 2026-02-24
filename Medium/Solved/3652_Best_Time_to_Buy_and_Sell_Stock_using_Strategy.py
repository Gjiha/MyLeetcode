class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        originalValue = 0
        newValue = 0
        n = len(prices)
        for i in range(n):
            originalValue += (prices[i]*strategy[i])
            if i < k//2:
                newValue += 0
            elif i < k:
                newValue += prices[i]
            elif i >= k:
                newValue += (prices[i]*strategy[i])
        
        tempValue = newValue
        for i in range(1,n-k+1):
            if strategy[i-1] == -1:
                tempValue -= prices[i-1]
            elif strategy[i-1] == 1:
                tempValue += prices[i-1]
            tempValue -= prices[i-1+(k//2)]
            if strategy[i + k-1] == -1:
                tempValue += 2 * prices[i+k-1]
            elif strategy[i + k-1] == 0:
                tempValue += prices[i+k-1]
            
            newValue = max(tempValue, newValue)

        return max(originalValue, newValue)
        
        
sol = Solution()
p = [4,2,8]
s = [-1,0,1]
k = 2
print(sol.maxProfit(p,s,k))