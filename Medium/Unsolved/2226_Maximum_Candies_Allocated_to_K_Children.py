class Solution:

    def checkSolution(self, list: list[int], parameter: int, goal: int) -> bool:
        total = 0
        for pile in list:
            toal += pile//parameter
        if total > parameter:
            return True
        else:
            return False 
    
    def binarySearch(self, list: list[int], start: int, end:int):
        m = 


    def maximumCandies(self, candies: list[int], k: int) -> int:
        maxCandies = sum(candies)//k
        candies.sort()


