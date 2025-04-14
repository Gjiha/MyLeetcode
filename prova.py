class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        n = len(nums) 
        if n == 1:
            return 0
        
        minDiff = float('inf')
        maxDiff = float('-inf')
        nums.sort()

        for i in range(1,n):
            newDiff = abs(nums[i] - nums[i-1])
            if newDiff < minDiff:
                minDiff = newDiff
        
        for i in range(n):
            for j in range(i,n):
                newDiff = abs(nums[i] - nums[j])
                if abs(newDiff - 2*k) < abs(maxDiff - 2*k):
                    maxDiff = newDiff
                    
        
        if minDiff < abs(maxDiff - 2*k):
            return minDiff
        else:
            return maxDiff