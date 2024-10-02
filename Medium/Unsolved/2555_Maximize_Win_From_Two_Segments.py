import heapq

class Solution:
    def binmax(self, array: list[int], start: int, end: int, value: int):
        if start > end:
            return -1
        medium = start + (end - start) // 2

        if array[medium] == value and (medium == len(array)-1 or array[medium + 1] > value) or (array[medium] < value and (medium == len(array) - 1 or array[medium + 1] > value)):
            return medium
        
        elif array[medium] <= value:
            return self.binmax(array, medium + 1, end, value)
        
        elif array[medium] >= value:
            return self.binmax(array, start, medium - 1, value)
    
    def binmin(self, array: list[int], start: int, end: int, value: int):
        if start > end:
            return -1

        medium = start + (end - start) // 2
    
        if array[medium] == value and (medium == 0 or array[medium - 1] < value) or (array[medium] > value and (medium == len(array) - 1 or array[medium - 1] < value)):
            return medium

        elif array[medium] >= value:
            return self.binmin(array, start, medium - 1, value)

        elif array[medium] <= value:
            return self.binmin(array, medium + 1, end, value)


    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        
        firstValue = 0
        secondValue = 0

        minPrize = prizePositions[0]
        interval = [minPrize , minPrize + k]
        while interval[1] < prizePositions[-1]:
            print(interval)

            start = self.binmin(prizePositions, 0, len(prizePositions) - 1, interval[0])
            end = self.binmax(prizePositions, 0, len(prizePositions) - 1, interval[1])

            numberOfPrize = end - start + 1

            if firstValue <= secondValue and numberOfPrize >= firstValue:
                firstValue = numberOfPrize
            elif secondValue <= firstValue and numberOfPrize >= secondValue:
                secondValue = numberOfPrize
            
            if k == 0:
                interval[0] += 1
                interval[1] += 1
            else:    
                interval[0] = interval[1]
                interval[1] += k
                
        
        return firstValue + secondValue


x = [1,1,2,2,3,3,5]
sol = Solution()
print(sol.maximizeWin(x, 2))