ENUM = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def ric(self, grid: list[list[int]], value: str, pos: tuple[int, int], oldPos: tuple[int, int]):
        y, x = pos
        
        if pos in self.visited and oldPos != pos:
            return True
        
        self.visited.add(pos)
        for couples in ENUM:
            newPos = (y + couples[0], x + couples[1])
            if (newPos != oldPos) and (0 <= newPos[0] <= self.maxRow and 0 <= newPos[1] <= self.maxCol):
                if grid[newPos[0]][newPos[1]] == value:
                    if self.ric(grid, value, newPos, pos):
                        return True
        return False

        
        
        
    def containsCycle(self, grid: list[list[str]]) -> bool:
        self.maxRow = len(grid) - 1
        self.maxCol = len(grid[0]) - 1
        self.visited = set()
        for i in range(self.maxRow):
            for j in range(self.maxCol):
               if (i, j) not in self.visited:
                    if self.ric(grid, grid[i][j], (i,j), (-1,-1)):
                        return True
        return False
        
sol = Solution()
p = sol.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]])
print(p)