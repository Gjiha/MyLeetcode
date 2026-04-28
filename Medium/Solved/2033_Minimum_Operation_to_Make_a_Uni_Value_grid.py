class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:

        listOfNum = []
        reminder = grid[0][0] % x

        for row in grid:
            for y in row:
                if y % x != reminder:
                    return -1
                listOfNum.append(y)
        
        listOfNum.sort()

        medianPos = len(listOfNum)//2
        median = listOfNum[medianPos]

        move = 0

        for num in listOfNum:
            move += abs(num - median)//x
        return move