
UP = set([2,3,4])
RIGHT = set([1,3,5])
DOWN = set([2,5,6])
LEFT = set([1,4,6])

LEGALMOVE = {
    1: [LEFT, RIGHT],
    2: [UP, DOWN],
    3: [LEFT, DOWN],
    4: [DOWN, RIGHT],
    5: [UP, LEFT],
    6: [UP, RIGHT]
}

ENUM = [
    ((-1, 0), UP),
    ((0, 1), RIGHT),
    ((1, 0), DOWN),
    ((0, -1), LEFT)
]
class Solution:

    def ric(self, pos: tuple[int, int]):
        if pos in self.visited:
            return
        y, x = pos
        self.visited.add(pos)

        typeOfStreet = self.grid[y][x]

        for direction, possibility in ENUM:
            if possibility in LEGALMOVE[typeOfStreet]:
                newPos = (y + direction[0], x + direction[1])
                if (0 <= newPos[0] <= self.m and 0 <= newPos[1]<= self.n):
                    if self.grid[newPos[0]][newPos[1]] in possibility:
                        self.ric(newPos)
        
        self.valid.add(pos)
        return



    def hasValidPath(self, grid: list[list[int]]) -> bool:
        self.visited = set()
        self.valid = set([(0,0)])
        self.grid = grid
        self.m = len(grid) - 1
        self.n = len(grid[0]) - 1
        
        self.ric((0,0))
        print(self.valid)
        print(self.visited)
        return (self.m,self.n) in self.valid

sol = Solution()
print(sol.hasValidPath([[2,4,3],[6,5,2]]))