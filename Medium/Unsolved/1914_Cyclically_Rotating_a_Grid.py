class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid) - 1
        n = len(grid[0]) - 1
