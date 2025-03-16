class Solution:

    def checkSolution(self, list: list[int], parameter: int, goal: int) -> bool:
        total = 0
        for pile in list:
            total += pile//parameter
        
        if total >= goal:
            return True
        
        return False 
    
    def binarySearch(self, list: list[int], start: int, end:int, goal: int) -> int:
        while start <= end:
            m = start + (end - start)//2
            var = self.checkSolution(list, m, goal)

            if var:
                return max(m, self.binarySearch(list, m+1, end, goal))
            
            return self.binarySearch(list, start, m-1, goal)
            
        return 0



    def maximumCandies(self, candies: list[int], k: int) -> int:
        maxCandies = sum(candies)//k
        if maxCandies < 1:
            return 0
        candies.sort()
        return self.binarySearch(candies, 1, maxCandies, k)

sol = Solution()
x = sol.maximumCandies([4,7,5], 16)
print(x)